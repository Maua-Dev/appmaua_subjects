from src.domain.errors.errors import UnexpectedError
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetFinalScoreUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, codeSubject: str, academicYear: int, idStudent: int) -> tuple:
        try:

            if codeSubject is None:
                raise Exception('codeSubject is None')

            if idStudent is None:
                raise Exception('idStudent is None')

            if academicYear is None:
                raise Exception('academicYear is None')

            subject = await self._subjectRepository.getSubjectByCode(codeSubject.upper())
            if subject is None:
                raise Exception('codeSubject is invalid')

            isPartialScore = False

            testQnt = await self._subjectRepository.getEvalQuantityByType(codeSubject.upper(), academicYear,
                                                                          20)  # Qnt Provas
            workQnt = await self._subjectRepository.getEvalQuantityByType(codeSubject.upper(), academicYear,
                                                                          19)  # Qnt Trabalhos
            subQnt = await self._subjectRepository.getEvalQuantityByType(codeSubject.upper(), academicYear,
                                                                         21)  # Qnt Subs

            testScores = []
            workScores = []
            subScores = []

            partialTestWeights = []
            partialWorkWeights = []

            # Notas e pesos de cada prova
            for i in range(1, testQnt + 1):
                testScores.append(await self._subjectRepository.getSubjectScoreByEvalType(codeSubject.upper(),
                                                                                          idStudent,
                                                                                          academicYear,
                                                                                          i))
                partialTestWeights.append(await self._subjectRepository.getEvalWeightByType(codeSubject.upper(),
                                                                                            academicYear,
                                                                                            i))
                # index da lista define a prova
                # testScores[n] = P(n+1)

            # Notas e pesos de cada trabalho
            for j in range(7, workQnt + 7):
                workScores.append(await self._subjectRepository.getSubjectScoreByEvalType(codeSubject.upper(),
                                                                                          idStudent,
                                                                                          academicYear,
                                                                                          j))
                partialWorkWeights.append(await self._subjectRepository.getEvalWeightByType(codeSubject.upper(),
                                                                                            academicYear,
                                                                                            j))
                # index da lista define o trabalho
                # workScores[n] = T(n+1)

            # Notas e pesos de cada PSub
            for k in range(5, subQnt + 5):
                subScores.append(await self._subjectRepository.getSubjectScoreByEvalType(codeSubject.upper(),
                                                                                         idStudent,
                                                                                         academicYear,
                                                                                         k))
                # index da lista define a sub
                # subScores[n] = PS(n+1)

            """   Avalia existencia de notas sub p substituir provas (caso a sub seja maior que a prova a qual ela substitui
              e não tenha nota -1 (cola) para essa prova)"""
            for score in range(len(subScores)):
                if subScores[score] is not None:
                    testsToReplace = await self._subjectRepository.getWichScoreToReplace(codeSubject.upper(),
                                                                                         academicYear,
                                                                                         score + 5)
                    if testsToReplace is not None:
                        for test in testsToReplace:
                            if ((testScores[test - 1] < subScores[score])
                                    and (testScores[test - 1] != -1)):
                                testScores[test - 1] = subScores[score]

            totalPartialTestWeight = sum(partialTestWeights)
            totalPartialWorkWeight = sum(partialWorkWeights)

            finalTestWeight = await self._subjectRepository.getEvalWeightByType(codeSubject.upper(),
                                                                                academicYear,
                                                                                20)
            finalWorkWeight = await self._subjectRepository.getEvalWeightByType(codeSubject.upper(),
                                                                                academicYear,
                                                                                19)
            # Calculo da media de provas
            aux = 0
            for i in range(len(testScores)):
                if testScores[i] is not None and testScores[i] >= 0:
                    aux += testScores[i] * partialTestWeights[i]
                else:
                    isPartialScore = True
            testAverage = aux / totalPartialTestWeight

            # Calculo da media de trabalho
            aux = 0
            for i in range(len(workScores)):
                if workScores[i] is not None and workScores[i] >= 0:
                    aux += workScores[i] * partialWorkWeights[i]
                else:
                    isPartialScore = True
            workAverage = aux / totalPartialWorkWeight

            finalAverage = (testAverage * finalTestWeight + workAverage * finalWorkWeight) / (finalTestWeight +
                                                                                              finalWorkWeight)

            # Retorna nota truncada e se é parcial
            return float(str(finalAverage)[:str(finalAverage).index('.')+2]), isPartialScore
        except Exception as error:
            raise UnexpectedError('GetFinalScoreUsecase', str(error))
