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

def actualizar_tema(db: Session, tema_id: int, nuevos_datos: dict):
    tema_existente = db.get(Topic, tema_id)
    try:
        if tema_existente:
            tema_existente.titulo = nuevos_datos.get('titulo', tema_existente.titulo)
            tema_existente.contenido = nuevos_datos.get('contenido', tema_existente.contenido)
            tema_existente.comandos = nuevos_datos.get('comandos', tema_existente.comandos)
            tema_existente.sesion = nuevos_datos.get('sesion', tema_existente.sesion)
            tema_existente.categoria = nuevos_datos.get('categoria_id', tema_existente.categoria)
            db.commit()
            db.refresh(tema_existente)
    except Exception as e:
        db.rollback()
        print(f'El tema no se actualizo debido a {e}')
        return None
    return tema_existente

def eliminar_tema(db: Session, tema_id: int):
    tema_a_eliminar = db.get(Topic, tema_id)
    try:
        if tema_a_eliminar:
            db.delete(tema_a_eliminar)
            db.commit()
            return True
    except Exception as e:
        db.rollback()
        print(f'El tema no se elimino debidoa a {e}')
    return False
