from database import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey

class Progreso(Base):
    __tablename__ = 'progreso'
    id = Column(
        'id_progreso',
        Integer,
        primary_key=True
    )
    usuario = Column(
        'id_usuario',
        Integer,
        ForeignKey('usuarios.id_usuario', ondelete='CASCADE'),
        nullable=False
    )
    tema = Column(
        'id_tema',
        Integer,
        ForeignKey('temas.id_tema', ondelete='CASCADE'),
        nullable=False
    )
    fecha = Column(
        'ultima_practica',
        DateTime
    )
    repeticiones = Column(
        'veces_repasado',
        Integer,
        nullable=False,
        default=0
    )