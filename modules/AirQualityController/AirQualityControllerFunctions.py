import sys

def getParticleIndex(self):
    return self.particleIndexes

def checkParticles(self, particle):
    if particle in self.particleIndexes:
        if self.particles[particle] == None:
            return False
        else:
            return True
    else:
        print(f"Error: {particle} is not a valid particle parameter.")
        sys.exit(1)

def getParticleName(self, particle):
    if particle in self.particleIndexes:
        return self.particleNames[particle]
    
def setParticle (self, particle, amnt):
    if self.checkParticles (particle):
        self.particles[particle] = amnt

def getQualityIndex(self, particle):
    if self.checkParticles (particle):
        amnt = self.particles[particle]
        thresholds = self.particleThreshold[particle]
        if amnt <= thresholds[0]:
            return self.qualityIndexes[0]
        elif amnt <= thresholds[1]:
            return self.qualityIndexes[1]
        elif amnt <= thresholds[2]:
            return self.qualityIndexes[2]
        elif amnt <= thresholds[3]:
            return self.qualityIndexes[3]
        else:
            return self.qualityIndexes[4]

def getHighestIndexDefinition(self):
    values = []
    weights = {
        'Boa': 0,
        'Moderada': 1,
        'Ruim': 2,
        'Muito Ruim': 3,
        'Péssima': 4
    }

    for particle in self.particleIndexes:
        values.append(self.getQualityIndex(particle))

    max_value = max(values, key=lambda x: weights[x])
    return [max_value, self.qualityIndexesDefinitions[max_value]]

#Use later
def getWorstComponents(self):
    worstResult = getHighestIndexDefinition(self)[0]
    worstCompoents = [];
    for particle in self.particleIndexes:
        if self.getQualityIndex(particle) == worstResult:
            worstCompoents.append(particle)
    return worstCompoents

def getAllParticles(self):
    return self.particles