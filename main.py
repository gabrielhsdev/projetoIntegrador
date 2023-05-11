from modules.AirQualityController.AirQualityController import AirQualityController

analyze_air_quality = AirQualityController()
particleData = analyze_air_quality.getParticleIndex()
particleIndexes = particleData
looping = True

while looping:

    #   set particles12
    for particle in particleIndexes:
        particleName = analyze_air_quality.getParticleName(particle)
        print(f"Atribua o valor para a particula '{particleName}'({particle}):")
        amnt = int(input())
        analyze_air_quality.setParticle(particle, amnt)

    #   calculate quality index
    print("\n\n\nCalculando o indice de qualidade.\n")
    for particle in particleIndexes:
        particleName = analyze_air_quality.getParticleName(particle)
        particleQuality = analyze_air_quality.getQualityIndex(particle)
        #   print(f"O indice de qualidade para '{particleName}'({particle}) é {particleQuality}")
    
    #   get worst index AND its definition
    highestIndex = analyze_air_quality.getHighestIndexDefinition()
    print(f"O índice de qualidade do ar é {highestIndex[0]}\nDef: {highestIndex[1]}\n\n")

    #   ask if user wants to continue
    print("Deseja continuar? (s/n)")
    answer = input()
    if answer == 'n' or answer == 'N':
        looping = False

