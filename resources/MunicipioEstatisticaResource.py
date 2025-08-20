from flask_restful import Resource
from models import MunicipioEstatistica

def serialize(model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

class MunicipioEstatisticaResource(Resource):
    def get(self, municipio_id):
        estatisticas = MunicipioEstatistica.query.filter_by(cod_municipio=municipio_id).all()
        return [serialize(e) for e in estatisticas], 200
