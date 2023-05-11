from modules.AirQualityController.AirQualityController import AirQualityController
from modules.database.database_connection import dbPDO

db = dbPDO()
analyze_air_quality = AirQualityController()
particleIndexes = analyze_air_quality.getParticleIndex()
looping = True

#Read data and set its values
averages = {}
for particle in particleIndexes:
    query = f"SELECT ROUND(AVG({particle}), 2) FROM air_information"
    result = db.query(query, fetchall=True)
    avgParticle = result[0][0] if result[0][0] is not None else 0
    averages[particle] = avgParticle
print(averages)

while looping:

    #   Read Particles 
    for particle in particleIndexes:
        analyze_air_quality.setParticle(particle, averages[particle])
    
    #   get worst index AND its definition
    highestIndex = analyze_air_quality.getHighestIndexDefinition()
    print(f"O índice de qualidade do ar é: {highestIndex[0]}\nDef: {highestIndex[1]}\n\n")

    #   ask if user wants to continue
    print("Deseja ler novamente ? (s/n)")
    answer = input()
    if answer == 'n' or answer == 'N':
        looping = False

