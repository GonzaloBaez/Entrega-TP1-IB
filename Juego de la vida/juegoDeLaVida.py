
import os
import time
import random

score = 0
rivalScore = 10
rivalName = 'RNA'


def showScore():
    customPrint(
        "---------------------------------------------------------------------------------------------------------")
    
    customPrint(
            f"{rivalName} obtuvo {rivalScore} y {name} {score}")
    if score > rivalScore:
        customPrint(f"EL GANADOR ES {name}")
        customPrint(f"")
        customPrint(f"")
        customPrint('           y͓̌â͎ ͮͩ͒ͯͣno͖̙̖͔͇̎͊̐ͪ̾́ͅs̺̟̺ͩ͗ͦ ̭̀v̯̆o̹ͬl͊͛ͩ́̃̓v͍͔̹̘̩̺́͊̈ͩ́̔e͚͎̭̪̳̬͍͑ͨ̂̿̿ͨ͆r͎̗̟͉͕̖ͮ̉͒͆ͧ͂em͂ͯ́̿̂ͭo̭̼̙̱͆̔͑̑š̊̎ͯ̿̄ ̠̫͙a͇̪͙̅͆̒ ̲̲̝̓̇ͮe͕͎͈̳͓͎̿ͧ͛ͨ̀́n̽ͯc͔̮̩̤ͤͫͥ͑ỏ̹̠̏n͇ͧt͉̲̟̖̮̘r̝͛a͎̯̯̤̬r̜̘̩͔̮̺͕..̺̥̥͖͈̫̫̉̓͋̉̾ͬ̾.̗̇.....')
        customPrint('(◣_◢)')
    else:
        customPrint(f"EL GANADOR ES {rivalName}")
        customPrint('           ℕ𝕠 𝕖𝕤𝕡𝕖𝕣𝕒𝕓𝕒 𝕠𝕥𝕣𝕠 𝕣𝕖𝕤𝕦𝕝𝕥𝕒𝕕𝕠')
        customPrint('(▀_▀)')
    customPrint(
        "---------------------------------------------------------------------------------------------------------")
    customPrint(
        "    ")
    customPrint(
        "    ")


def customPrint(message):
    print(message)


def customInput(message):
    myInput = input(message)
    if (myInput == "SALIR"):
        raise Exception()
    return myInput


def multipleChoice(question, answers, correctNumber, points):
    global score
    global rivalScore
    customPrint(f' {question}')
    for index, value in enumerate(answers):
        customPrint(f'{index + 1} - {value}')
    myInput = int(customInput("> "))
    time.sleep(2)
    if (myInput == correctNumber):
        score += points
        customPrint("----------------------------\n")
        customPrint("Excelente!!!! Acertaste!!!\n")
    else:
        customPrint(
            f'Mm esa opción no es correcta')

    customPrint(f'Turno de {rivalName}')
    time.sleep(2)
    rivalAnswer = random.choice(answers)
    customPrint(f'El rival respondio: {rivalAnswer}')
    time.sleep(1)
    if(answers.index(rivalAnswer) + 1 == correctNumber):
        rivalScore += points
        customPrint(f"Excelente!!!! {rivalName} acerto!!!\n")
        customPrint("----------------------------\n")
    else:
        customPrint(
            f'Mm esa opción no es correcta')
        customPrint(
            "------------------------------------------------------------------------------------")
    time.sleep(2)

def clearConsole():
    return os.system('clear')


def stepOne():
    customPrint(f' Excelente {name}  A JUGAR!!!')
    time.sleep(2)
    customPrint(' Empecemos con preguntas sencillas!')
    multipleChoice("Cuantos tipos de células existen?", [
        "Una", "Dos", "Infinitas"], 2, 1)
    multipleChoice("Cual fue la primera en aparecer?", [
        "Eucariota", "Procariota", "Las dos aparecieron al mismo tiempo"], 2, 1)
    multipleChoice("Cuantos flagelos tiene una Celula Eucariota?", [
        "Uno", "Dos", "No tiene"], 3, 1)


def stepTwo():
    customPrint(f'Ahora vamos a complicarlo un poco..')
    multipleChoice("Cuales son los pasos de la expresión génica?", [
        "Transcripción y traducción", "Transferencia y transcripción", "Traducción y transferencia"], 1, 20)
    multipleChoice("Cuales de los siguientes nombres no identifica un aminoacido?", [
        "Asparato", "Alanina", "Serina", "Recina"], 4, 20)





try:
    customPrint('--------------------------------------')
    customPrint(' EL JUEGO DE LA VIDA')
    customPrint('              ')
    customPrint(' Bienvenido al Juego de la Vida. Juego que desafia tus conocimientos sobre la expresion Genica.')
    customPrint(f' Para hacerlo aun mas desafiante y competitivo, jugaras contra un robot llamado {rivalName} (Robot No Amigable).')
    customPrint('Dicho Robot se encarga de encriptar la informacion importante de las personas y pedirles dinero a cambio para recuperarlo...')
    customPrint('(◣_◢)')
    customPrint(' Aunque tambien le gusta la biologia.')
    customPrint('(▀_▀)')

    customPrint('')
    customPrint(' Las reglas son simples, cada respuesta correcta da puntos, el que mas puntos obtenga al final del juego gana. Listo?')
    customPrint('--------------------------------------')
    name = customInput(' Pero antes, dinos tu nombre:\n> ')
    customPrint(' ')
    #stepOne()
    customPrint(' ')
    #stepTwo()
    customPrint(' ')
    showScore()
except:
    customPrint('')





