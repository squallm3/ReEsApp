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
            base = {'id_tema': tema.id, 'sesion_tema': tema.sesion, 'contenido_tema': tema.contenido,
                                  'comandos_tema': tema.comandos, 'categoria_tema': tema.categoria}
            version_pendiente = {'id_progreso': None, 'usuario_progreso': None, 'tema_progreso': None,
                                  'fecha_progreso': None, 'repeciones_progreso': None }
            version_historial = {'id_progreso': progreso.id, 'usuario_progreso': progreso.usuario, 'tema_progreso': progreso.tema,
                                  'fecha_progreso': progreso.fecha, 'repeticiones_progreso': progreso.repeticiones}
            if progreso is None:
                pendiente.append(base | version_pendiente)
            else:
                historial.append(base | version_historial)
    pendiente_sorted = sorted(pendiente, key= lambda x: x['id_tema'])
    historial_sorted = sorted(historial, key= lambda x: x['fecha_progreso'], reverse=True)
    return {'pendiente': pendiente_sorted, 'historial': historial_sorted}

def generar_mix_repaso(usuario_id, categoria_id):
    pendiente_historial = obtener_listas_dashboard(usuario_id, categoria_id)
    temas_fijos = pendiente_historial['historial'][0:4]
    temas_azar = pendiente_historial['historial'][4:]
    temas_a_elegir = min(4, len(temas_azar))
    temas_azar_salida = random.sample(temas_azar, temas_a_elegir)
    temas_fijos_azar_salida = temas_fijos + temas_azar_salida
    return temas_fijos_azar_salida