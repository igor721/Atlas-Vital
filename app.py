from helpers.database import app, db
from flask_restful import Api
from flask_migrate import Migrate

# Importa os resources
from resources.RegiaoResource import RegiaoResource
from resources.UfResouce import UfResource
from resources.MesorregiaoResource import MesorregiaoResource
from resources.MicrorregiaoResource import MicrorregiaoResource
from resources.MunicipioResource import MunicipioResource
from resources.UfEstatisticaResource import UfEstatisticaResource
from resources.MunicipioEstatisticaResource import MunicipioEstatisticaResource

# Inicializa API e Migrate
api = Api(app)
migrate = Migrate(app, db)

# Rotas da API
api.add_resource(RegiaoResource, "/regioes")
api.add_resource(UfResource, "/ufs")
api.add_resource(MesorregiaoResource, "/mesorregioes")
api.add_resource(MicrorregiaoResource, "/microrregioes")
api.add_resource(MunicipioResource, "/municipios")
api.add_resource(UfEstatisticaResource, "/ufs/<int:uf_id>/estatisticas")
api.add_resource(MunicipioEstatisticaResource, "/municipios/<int:municipio_id>/estatisticas")

if __name__ == "__main__":
    app.run(debug=True)
