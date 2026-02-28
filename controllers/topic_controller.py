from sqlalchemy.orm import Session
from models.topics import Topic

def crear_tema(db: Session, tema_data: dict):
    try:
        nuevo_tema = Topic()
        nuevo_tema.titulo = tema_data['titulo']
        nuevo_tema.contenido = tema_data['contenido']
        nuevo_tema.comandos = tema_data['comandos']
        nuevo_tema.sesion = tema_data['sesion']
        nuevo_tema.categoria = tema_data['categoria_id']
        db.add(nuevo_tema)
        db.commit()
        db.refresh(nuevo_tema)
    except Exception as e:
        db.rollback()
        print(f"El tema no se creo debido a: {e}")
        return None
    print(f"Tema {nuevo_tema.id} creado.")
    return nuevo_tema

def obtener_tema(db: Session, tema_id: int):
    return db.get(Topic, tema_id)
