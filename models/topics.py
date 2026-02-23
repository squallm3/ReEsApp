from database import Base
from sqlalchemy import Column, Integer, String, Text

class Topic(Base):
    __tablename__ = 'temas'
    id = Column(
        'id_tema',
        Integer,
        primary_key=True
    )
    sesion = Column(
        'nombre_sesion',
        String(100),
        unique=True,
        nullable=False
    )
    contenido = Column(
        'contenido',
        Text,
        nullable=False
    )
    comandos = Column(
        'comandos',
        Text
    )