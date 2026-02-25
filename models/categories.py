from models.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

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
    temas_relationship = relationship('Topic', back_populates='categorias_relationship')