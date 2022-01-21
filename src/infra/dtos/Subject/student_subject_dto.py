from sqlalchemy import Column, ForeignKey, Integer
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class StudentSubjectDTO(Base):
    __tablename__ = 'StudentSubjects'

    id = Column(Integer, primary_key=True)
    idStudent = Column(Integer, nullable=False)
    idSubject = Column(Integer, ForeignKey('Subjects.id'))