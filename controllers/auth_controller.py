from models.database import get_db
from models.users import Usuario

def validar_login(nombre, clave):
    with get_db() as db:
        query_usuario = db.query(Usuario).filter_by(nombre=nombre).first()
        if query_usuario and clave == query_usuario.clave:
            return query_usuario
        return None