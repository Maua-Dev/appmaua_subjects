from sqlalchemy import Column, ForeignKey, Integer
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class StudentSubjectDTO(Base):
    __tablename__ = 'StudentCourse'

    id = Column(Integer, primary_key=True)
    idAluno = Column(Integer, nullable=False)
    idCourse = Column(Integer, ForeignKey('Courses.id'))

    def getId(self) -> int:
        return self.id

    def getIdAluno(self) -> int:
        return self.idAluno

    def getIdCourse(self) -> int:
        return self.idCourse