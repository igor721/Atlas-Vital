from flask_restful import Resource
from models import Municipio

def serialize(model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

class MunicipioResource(Resource):
    def get(self):
        municipios = Municipio.query.all()
        return [serialize(m) for m in municipios], 200
