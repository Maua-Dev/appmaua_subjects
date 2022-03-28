from sqlalchemy import Column, String, Integer
from src.domain.entities.course import Course
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class SubjectDTO(Base):
    __tablename__ = 'Courses'

    id = Column(Integer, primary_key=True)
    codeCourse = Column(String, nullable=False)
    name = Column(String, nullable=False)

    def toEntity(self) -> Course:
        return Course(
            codeCourse=self.codeCourse,
            name=self.name
        )

    def getId(self) -> int:
        return self.id

    def getCodeCourse(self) -> str:
        return self.codeCourse

    def getName(self) -> str:
        return self.name