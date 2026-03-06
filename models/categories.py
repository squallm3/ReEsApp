from models.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

class Categoria(Base):
    __tablename__ = 'categorias'
    id: Mapped[int] = mapped_column('id_categoria', primary_key=True)
    nombre: Mapped[str] = mapped_column('nombre_categoria', String(50), unique=True, nullable=False)
    temas_relationship: Mapped[list["Topic"]] = relationship('Topic', back_populates='categorias_relationship')
