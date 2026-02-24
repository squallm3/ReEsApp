from database import Base
from sqlalchemy import Column, Integer, String

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(
        'id_categoria',
        Integer,
        primary_key=True
    )
    nombre = Column(
        'nombre_categoria',
        String(50),
        unique=True,
        nullable=False
    )
