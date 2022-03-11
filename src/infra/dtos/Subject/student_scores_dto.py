from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.infra.dtos.db_base import Base


class StudentScoresDTO(Base):
    __tablename__ = 'StudentScores'

    id = Column(Integer, primary_key=True)
    idStudent = Column(ForeignKey('StudentSubjects.id'), nullable=False)
    codeSubject = Column(ForeignKey('Subjects.codeSubject'), nullable=False)
    value = Column(Float, nullable=True)
    academicYear = Column(Integer, nullable=False)
    idEvaluationType = Column(ForeignKey('EvalType.id'), nullable=False)

    evalType = relationship("EvalTypeDTO")
    subjects = relationship("SubjectDTO")
    students = relationship('StudentSubjectDTO')
