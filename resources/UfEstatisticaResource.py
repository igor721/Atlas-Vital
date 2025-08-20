from flask_restful import Resource
from models import UfEstatistica

def serialize(model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

class UfEstatisticaResource(Resource):
    def get(self, uf_id):
        estatisticas = UfEstatistica.query.filter_by(cod_uf=uf_id).all()
        return [serialize(e) for e in estatisticas], 200
