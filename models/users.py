from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(
        'id_usuario',
        Integer,
        primary_key=True
    )
    nombre = Column(
        'nombre_usuario',
        String(50),
        unique=True,
        nullable=False
    )
    clave = Column(
        'clave_encriptada',
        String(255),
        nullable=False
    )
    admin = Column(
        'es_admin',
        Boolean,
        default=False
    )
    progresos_relationship = relationship('Progreso', back_populates='usuario_relationship', cascade='all, delete-orphan')

