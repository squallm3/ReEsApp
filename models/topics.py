from database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

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
    categoria = Column(
        'id_categoria',
        Integer,
        ForeignKey('categorias.id_categoria')
    )
    progresos_relationship = relationship('Progreso', back_populates='tema_relationship', cascade='all, delete-orphan')
    categorias_relationship = relationship('Categoria', back_populates='temas_relationship')


