import bcrypt

def verificar_password(password_plano: str, password_hasheado: str):
    password_bytes = password_plano.encode('utf-8')
    hash_bytes = password_hasheado.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hash_bytes)
