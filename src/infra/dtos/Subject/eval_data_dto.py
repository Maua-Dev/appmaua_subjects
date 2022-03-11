from sqlalchemy import Column, Integer, String, ForeignKey
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class EvalDataDTO(Base):
    __tablename__ = 'EvalData'

    id = Column(Integer, primary_key=True)
    idEvaluationType = Column(ForeignKey('EvalType.id'), nullable=False)
    codeSubject = Column(ForeignKey('Subjects.codeSubject'), nullable=False)
    quantity = Column(Integer, nullable=False)
    academicYear = Column(Integer, nullable=False)

    evalType = relationship("EvalTypeDTO")
    subjects = relationship("SubjectDTO")
