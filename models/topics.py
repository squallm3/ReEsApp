from models.database import Base
from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional

class Topic(Base):
    __tablename__ = 'temas'
    id: Mapped[int] = mapped_column('id_tema', Integer, primary_key=True)
    sesion: Mapped[str] = mapped_column('nombre_sesion', String(100), unique=True, nullable=False)
    contenido: Mapped[str] = mapped_column('contenido', Text, nullable=False)
    comandos: Mapped[Optional[str]] = mapped_column('comandos', Text, nullable=True)
    categoria: Mapped[int] = mapped_column('id_categoria', Integer, ForeignKey('categorias.id_categoria'))

    progresos_relationship: Mapped[list["Progreso"]] = relationship('Progreso', back_populates='tema_relationship', cascade='all, delete-orphan')
    categorias_relationship: Mapped["Categoria"] = relationship('Categoria', back_populates='temas_relationship')


