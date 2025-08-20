from helpers.database import app, db
from extrator import (
    apiParaSql_UF_SQLAlchemy,
    atualizarEstatisticasUFs,
    apiParaSql_Mesorregiao_SQLAlchemy,
    apiParaSql_Microrregiao_SQLAlchemy,
    apiParaSql_Municipio_SQLAlchemy,
    atualizarEstatisticasMunicipios,
    apiParaSql_Regiao_SQLAlchemy
)

if __name__ == "__main__":
    with app.app_context():
        # 1️⃣ Regiões primeiro (pais das UFs)
        apiParaSql_Regiao_SQLAlchemy()
        
        # 2️⃣ UFs dependem de Regiões
        apiParaSql_UF_SQLAlchemy()
        
        # 3️⃣ Estatísticas de UFs dependem das UFs
        atualizarEstatisticasUFs()
        
        # 4️⃣ Mesorregiões dependem das UFs
        apiParaSql_Mesorregiao_SQLAlchemy()
        
        # 5️⃣ Microrregiões dependem das Mesorregiões
        apiParaSql_Microrregiao_SQLAlchemy()
        
        # 6️⃣ Municípios dependem de UFs e Microrregiões
        apiParaSql_Municipio_SQLAlchemy()
        
        # 7️⃣ Estatísticas de Municípios dependem dos Municípios
        atualizarEstatisticasMunicipios()
    
    print("Importação completa de todos os dados.")
