from flask_restful import Resource
from models import Microrregiao

def serialize(model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

class MicrorregiaoResource(Resource):
    def get(self):
        microrregioes = Microrregiao.query.all()
        return [serialize(m) for m in microrregioes], 200
