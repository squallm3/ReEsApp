import bcrypt
from models.users import Usuario
from sqlalchemy.orm import Session

def verificar_password(password_plano: str, password_hasheado: str):
    password_bytes = password_plano.encode('utf-8')
    hash_bytes = password_hasheado.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hash_bytes)

def autenticar_usuario(db: Session, nombre: str, password_plano: str):
    usuario = db.query(Usuario).filter(Usuario.nombre == nombre).first()
    if not usuario:
        return None
    if verificar_password(password_plano, usuario.clave):
        return usuario
    return None
