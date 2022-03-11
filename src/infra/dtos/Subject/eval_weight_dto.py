from sqlalchemy import Column, Integer, String, ForeignKey
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class EvalWeightDTO(Base):
    __tablename__ = 'EvalWeight'

    id = Column(Integer, primary_key=True)
    idEvaluationType = Column(Integer, nullable=False)
    codeSubject = Column(String(5), nullable=False)
    weight = Column(Integer, nullable=False)
    academicYear = Column(Integer, nullable=False)
    replaces = Column(Integer, nullable=True)

