from typing import Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from src.envs import Envs
from src.infra.dtos.db_base import Base


class AsyncDBConnectionHandler:
    # session: Optional[sessionmaker]
    def __init__(self):
        self.__connection_string = Envs.getConfig().sqlConnection
        self.session: Optional[sessionmaker] = None

    def get_engine(self):
        engine = create_async_engine(self.__connection_string)
        return engine

    def __enter__(self):        
        engine = create_async_engine(self.__connection_string)
        self.session = sessionmaker(engine,expire_on_commit=False, class_=AsyncSession)
        # self.session = session_maker(bind=engine)
        # Base.metadata.create_all(engine)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):   
        if(isinstance(self.session,sessionmaker)):
            self.session.close() # pylint: disable=no-member