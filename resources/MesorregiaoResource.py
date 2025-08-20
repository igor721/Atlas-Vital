from flask_restful import Resource
from models import Mesorregiao

def serialize(model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

class MesorregiaoResource(Resource):
    def get(self):
        mesorregioes = Mesorregiao.query.all()
        return [serialize(m) for m in mesorregioes], 200
