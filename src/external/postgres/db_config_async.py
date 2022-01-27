from typing import Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from src.envs import Envs
from src.infra.dtos.db_base import Base


class AsyncDBConnectionHandler:
    # session: Optional[sessionmaker]
    def __init__(self):
        self.__connection_string = Envs.getConfig().sqlConnection
        engine = create_async_engine(self.__connection_string,echo=True)
        self.session = sessionmaker(engine,expire_on_commit=False, future=True, class_=AsyncSession)