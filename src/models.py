from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Client(Base):
    """
    Create Client Model
    Un modelo es la representación de una tabla en la base de datos.
    Describimos los campos que definen a un cliente.
    """
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, max_length=10, index=True, nullable=False) 
    is_active = Column(Boolean, default=True)

