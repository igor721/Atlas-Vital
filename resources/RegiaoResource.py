from flask_restful import Resource
from models import Regiao

def serialize(model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

class RegiaoResource(Resource):
    def get(self):
        regioes = Regiao.query.all()
        return [serialize(r) for r in regioes], 200
