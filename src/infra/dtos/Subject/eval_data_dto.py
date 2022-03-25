from sqlalchemy import Column, Integer, String, ForeignKey
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class EvalDataDTO(Base):
    __tablename__ = 'EvalData'

    id = Column(Integer, primary_key=True)
    idEvaluationType = Column(Integer, nullable=False)
    codeSubject = Column(String(5), nullable=False)
    quantity = Column(Integer, nullable=False)
    academicYear = Column(Integer, nullable=False)

    def getId(self) -> int:
        return self.id

    def getIdEvaluationType(self) -> int:
        return self.idEvaluationType

    def getCodeSubject(self) -> str:
        return self.codeSubject

    def getQuantity(self) -> int:
        return self.quantity

    def getAcademicYear(self) -> int:
        return self.academicYear
