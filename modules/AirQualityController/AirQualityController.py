from .AirQualityControllerFunctions import *

class AirQualityController:
  
    def __init__(self):

        self.particleIndexes = ['MP10', 'MP2.5', 'O3', 'CO', 'NO2', 'SO2']
        self.qualityIndexes = ['Boa', 'Moderada', 'Ruim', 'Muito Ruim', 'Péssima']

        self.qualityIndexesDefinitions = {
            'Boa': 'Qualidade do ar aceitável; nenhuma ação necessária.',
            'Moderada': 'Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.',
            'Ruim': 'Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.',
            'Muito Ruim': 'Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).',
            'Péssima': 'Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.'
        }

        self.particles = {
            'MP10': 0,
            'MP2.5': 0,
            'O3': 0,
            'CO': 0,
            'NO2': 0,
            'SO2': 0
        }

        self.particleNames = {
            'MP10': 'Partículas Inaláveis',
            'MP2.5': 'Partículas Inaláveis Finas',
            'O3': 'Ozônio',
            'CO': 'Monóxido de Carbono',
            'NO2': 'Dióxido de Nitrogênio',
            'SO2': 'Dióxido de Enxofre'
        }

        self.particleThreshold = {
            'MP10': [50, 100, 150, 250],
            'MP2.5': [25, 50, 75, 125],
            'O3': [9, 80, 160, 200],
            'CO': [200, 80, 120, 200],
            'NO2': [40, 80, 120, 200],
            'SO2': [40, 80, 120, 200]
        }

    def checkParticles(self, particle):
        return checkParticles(self, particle)

    def getParticleIndex(self):
        return getParticleIndex(self)
    
    def getParticleName(self, particle):
        return getParticleName(self, particle)

    def setParticle (self, particle, amnt):
        setParticle(self, particle, amnt)

    def getQualityIndex(self, particle):
        return getQualityIndex(self, particle)
    
    def getHighestIndexDefinition(self):
        return getHighestIndexDefinition(self)
    
    def getWorstComponents(self):
        return getWorstComponents(self)
        