from sqlalchemy import Column, ForeignKey, Integer
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class StudentCourseDTO(Base):
    __tablename__ = 'StudentCourse'

    id = Column(Integer, primary_key=True)
    idStudent = Column(Integer, nullable=False)
    idCourse = Column(Integer, ForeignKey('Courses.id'))
    courseYear = Column(Integer, nullable=False)
    academicYear = Column(Integer, nullable = False)

    def getId(self) -> int:
        return self.id

    def getIdAluno(self) -> int:
        return self.idAluno

    def getIdCourse(self) -> int:
        return self.idCourse

    def getCourseYear(self) -> int:
        return self.courseYear

    def getAcademicYear(self) -> int:
        return self.academicYear
