from sqlalchemy import Column, Integer, String, ForeignKey
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class EvalWeightDTO(Base):
    __tablename__ = 'EvalWeight'

    id = Column(Integer, primary_key=True)
    idEvaluationType = Column(Integer, nullable=False)
    codeSubject = Column(String(5), nullable=False)
    weight = Column(Integer, nullable=True)
    academicYear = Column(Integer, nullable=False)
    replaces = Column(Integer, nullable=True)

    def getId(self) -> int:
        return self.id

    def getIdEvaluationType(self) -> int:
        return self.idEvaluationType

    def getCodeSubject(self) -> str:
        return self.codeSubject

    def getWeight(self) -> int:
        return self.weight

    def getAcademicYear(self) -> int:
        return self.academicYear

    def getReplaces(self) -> int:
        return self.replaces