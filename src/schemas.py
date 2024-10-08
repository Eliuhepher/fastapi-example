from typing import Optional
from pydantic import BaseModel

class ClientBase(BaseModel):
    name: str
    email: str
    phone: str
    is_active: Optional [bool] = True

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    email: str

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True