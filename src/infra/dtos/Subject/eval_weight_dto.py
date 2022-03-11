from sqlalchemy import Column, Integer, String, ForeignKey
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class EvalWeightDTO(Base):
    __tablename__ = 'EvalWeight'

    id = Column(Integer, primary_key=True)
    idEvaluationType = Column(ForeignKey('EvalType.id'), nullable=False)
    codeSubject = Column(ForeignKey('Subjects.codeSubject'), nullable=False)
    weight = Column(Integer, nullable=False)
    academicYear = Column(Integer, nullable=False)
    replaces = Column(ForeignKey('EvalType.id'), nullable=True)

    evalType = relationship("EvalTypeDTO")
    subjects = relationship("SubjectDTO")

