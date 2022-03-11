from sqlalchemy import Column, Integer, String
from src.infra.dtos.db_base import Base


class EvalTypeDTO(Base):
    __tablename__ = 'EvalType'

    id = Column(Integer, primary_key=True)
    evalType = Column(String(50), nullable=False)
