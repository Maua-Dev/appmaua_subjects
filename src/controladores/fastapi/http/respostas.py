from pydantic import BaseModel


class ResRoot(BaseModel):
    deployment: dict
    controlador: dict

