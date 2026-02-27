from sqlalchemy.sql.elements import and_

from models.database import get_db
from models.topics import Topic
from models.progress import Progreso
import random

def obtener_temas_sesion(usuario_id, categoria_id):
    with get_db() as db:
        query_tema = db.query(Topic).filter_by(categoria=categoria_id).all()
        nuevos = []
        repaso = []
        for tema in query_tema:
            query_usuario_progreso = db.query(Progreso).filter_by(usuario=usuario_id, tema=tema.id).first()
            if query_usuario_progreso is None:
                nuevos.append(tema)
            else:
                repaso.append(tema)
        if len(repaso) < 4:
            final = nuevos[0:8]
            return final
        final = nuevos[0:4] + repaso[0:4]
        return final

def obtener_listas_dashboard(usuario_id, categoria_id):
    pendiente = []
    historial = []
    with get_db() as db:
        query_tema_progreso = (db.query(Topic, Progreso)
                               .outerjoin(Progreso, and_(Progreso.tema == Topic.id, Progreso.usuario == usuario_id))
                               .filter(Topic.categoria == categoria_id).all())
        for tema, progreso in query_tema_progreso:
            if progreso is None:
                pendiente.append((tema, progreso))
            else:
                historial.append((tema, progreso))
    pendiente_sorted = sorted(pendiente, key= lambda x: x[0].id)
    historial_sorted = sorted(historial, key= lambda x: x[1].fecha, reverse=True)
    return {'pendiente': pendiente_sorted, 'historial': historial_sorted}


# --- FUNCIÓN 2: EL MIX DE ESTUDIO (4+4) ---
# 4. 🧠 Creá 'generar_mix_repaso(usuario_id, categoria_id)':
#    - Buscá solo los temas que ya están en la tabla 'Progreso' para ese usuario/categoría.
#    - Ordenalos por la fecha de práctica más reciente.
#    - Tomá los primeros 4 (los "fijos" por ser los últimos movidos).
#    - Del resto de la lista (del 5to en adelante), usá random.sample() para elegir 4.
#    - Combiná ambos grupos y retorná la lista de 8.