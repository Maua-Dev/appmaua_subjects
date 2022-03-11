from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship

from src.infra.dtos.db_base import Base


class StudentScoresDTO(Base):
    __tablename__ = 'StudentScores'

    id = Column(Integer, primary_key=True)
    idStudent = Column(Integer, nullable=False)
    codeSubject = Column(String(5), nullable=False)
    value = Column(Float, nullable=True)
    academicYear = Column(Integer, nullable=False)
    idEvaluationType = Column(Integer, nullable=False)
