from flask_restful import Resource
from models import Uf

def serialize(model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

class UfResource(Resource):
    def get(self):
        ufs = Uf.query.all()
        return [serialize(u) for u in ufs], 200
