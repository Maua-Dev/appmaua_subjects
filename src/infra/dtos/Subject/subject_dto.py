from sqlalchemy import Column, String, Integer
from src.domain.entities.subject import Subject
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class SubjectDTO(Base):
    __tablename__ = 'Subjects'

    id = Column(Integer, primary_key=True)
    codeSubject = Column(String, nullable=False)
    name = Column(String, nullable=False)
    students = relationship('StudentSubjectDTO',
        cascade="all, delete",
        passive_deletes=True,
        backref="Subjects")
        def toEntity(self) -> Subject:
        return Subject(
            codeSubject=self.codeSubject,
            name=self.name
        )