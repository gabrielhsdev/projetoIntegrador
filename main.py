from modules.AirQualityController.AirQualityController import AirQualityController
from modules.database.database_connection import dbPDO
import os

db = dbPDO()
looping = True

while looping:

    print("\n\nEscolha dentre as opções abaixo:\n1 - Cadastro de amostras\n2 - Alteração de amostras\n3 - Exclusão de amostras\n4 - Classificação de amostras\n5 - Sair")
    opt = input("Digite o número da opção desejada:")
    print("------------------------------------------")
    match opt:
        
        case '1':
            print("Digite os valores, da amostra que voce quer cadastrar:\n")
            inputMp10 = input("MP10:")
            inputMp2_5 = input("MP2_5:")
            inputO3 = input("O3:")
            inputCO = input("CO:")
            inputNO2 = input("NO2:")
            inputSO2 = input("SO2:")
            query = f"INSERT INTO air_information (timestamp, MP10, MP2_5, O3, CO, NO2, SO2) VALUES (NOW(), {inputMp10}, {inputMp2_5},{inputO3},{inputCO},{inputNO2},{inputSO2});"
            result = db.query(query, fetchall=False)
            print('Inserido' if result == 1 else 'Não inserido')
            print (result)
            

        case '2':
            #pega o id da amostra que o usuario quer alterar
            print("Digite o id da amostra que deseja alterar:\n")
            idAlter = input()

            #pega os valores da amostra que o usuario quer alterar para mostrar
            query = f"SELECT * FROM air_information WHERE id = {idAlter};"
            result = db.query(query, fetchall=True)
            if len(result) == 0:
                print("Não existe amostra com esse id\n\n")
                break

            # Loop through rows
            for row in range(len(result)):
                # Loop through columns
                for col in range(len(result[row])):
                    print("{:<{width}}".format(str(result[row][col]), width=10), end=' | ')
                print()

            #pega os valores da amostra que o usuario quer alterar para alterar
            print("Digite os valores, da amostra que voce quer alterar:\n")
            inputMp10 = input("MP10:\n")
            inputMp2_5 = input("MP2_5:\n")
            inputO3 = input("O3:\n")
            inputCO = input("CO:\n")
            inputNO2 = input("NO2:\n")
            inputSO2 = input("SO2:\n")

            #altera os valores da amostra
            query = f"UPDATE air_information SET MP10 = {inputMp10}, MP2_5 = {inputMp2_5}, O3 = {inputO3}, CO = {inputCO}, NO2 = {inputNO2}, SO2 = {inputSO2} WHERE id = {idAlter};"
            result = db.query(query, fetchall=False)
            print('Alterado' if result == 1 else 'Não alterado, amostra nao existe ou id invalido')
            
        case '3':
            print("Digite o id da amostra que deseja excluir:")
            idDelete = input()
            query = f"DELETE FROM air_information WHERE id = {idDelete};"
            result = db.query(query, fetchall=False)
            print('Deletado' if result == 1 else 'Não deletado, amostra nao existe ou id invalido')

        case '4':
            #Show results 
            #Read data and set its values
            analyze_air_quality = AirQualityController()
            particleIndexes = analyze_air_quality.getParticleIndex()
            averages = {}
            for particle in particleIndexes:
                query = f"SELECT ROUND(AVG({particle}), 2) FROM air_information"
                result = db.query(query, fetchall=True)
                avgParticle = result[0][0] if result[0][0] is not None else 0
                averages[particle] = avgParticle
            print(averages)

            #   Read Particles 
            for particle in particleIndexes:
                analyze_air_quality.setParticle(particle, averages[particle])
            
            #   get worst index AND its definition
            highestIndex = analyze_air_quality.getHighestIndexDefinition()
            print(f"O índice de qualidade do ar é: {highestIndex[0]}\nDef: {highestIndex[1]}\n\n")

        case '5':
            looping = False

        case '100':
            query = f"SELECT * FROM air_information"
            result = db.query(query, fetchall=True)
            # Loop through rows
            for row in range(len(result)):
                # Loop through columns
                for col in range(len(result[row])):
                    # Print the cell value
                    print("{:<{width}}".format(str(result[row][col]), width=10), end=' | ')
                    
                # Print a new line after each row
                print()

        case _:
            print("\n\nOpção inválida\n\n")

    #   ask if user wants to continue
    print("Deseja continuar ? (s/n)")
    answer = input()
    if answer == 'n' or answer == 'N':
        looping = False
    if answer == 'n' or answer == 'N':
        looping = False
    os.system('cls')

