
import os
import time
import random

score = 0
rivalScore = 0
rivalName = 'RNA'
easyQ = []
hardQ = []
class Question:
    def __init__(self,quest,possibleAnswers,correctAnswer,points):
        self.quest = quest
        self.possibleAnswers = possibleAnswers
        self.correctAnswer = correctAnswer
        self.points = points

def showScore():
    customPrint(
        "---------------------------------------------------------------------------------------------------------")
    
    customPrint(
            f"{rivalName} obtuvo {rivalScore} y {name} {score}")
    if score > rivalScore:
        customPrint(f"EL GANADOR ES {name.upper()}")
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

    customPrint(f'Turno de {rivalName}\n')
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
    customPrint(f' Excelente {name} A JUGAR!!!')
    time.sleep(2)
    customPrint(' Empecemos con preguntas sencillas!')
    q1 = random.choice(easyQ)
    easyQ.remove(q1)
    q2 = random.choice(easyQ)
    easyQ.remove(q2)
    q3 = random.choice(easyQ)
    easyQ.remove(q3)
    multipleChoice(q1.quest,q1.possibleAnswers,q1.correctAnswer,q1.points)
    multipleChoice(q2.quest,q2.possibleAnswers,q2.correctAnswer,q2.points)
    multipleChoice(q3.quest,q3.possibleAnswers,q3.correctAnswer,q3.points)


def stepTwo():
    customPrint(f'Sencillas no? Veamos ahora..')
    
    q1 = random.choice(hardQ)
    hardQ.remove(q1)
    q2 = random.choice(hardQ)
    hardQ.remove(q2)
    multipleChoice(q1.quest,q1.possibleAnswers,q1.correctAnswer,q1.points)
    multipleChoice(q2.quest,q2.possibleAnswers,q2.correctAnswer,q2.points)





try:
    easyQ.append(Question("Cuantos tipos de células existen?",
        ["Una", "Dos", "Infinitas"],2,1))
    easyQ.append(Question("Cual fue el primer tipo de celula en aparecer?",
    ["Eucariota", "Procariota", "Las dos aparecieron al mismo tiempo"],2,1))
    easyQ.append(Question("Cuantos flagelos tiene una Celula Eucariota?",
    ["Uno", "Dos", "No tiene"],3,1))
    easyQ.append(Question("De que estan compuestas las proteinas?",
    ["Aminoacidos", "Celulas", "Otras proteinas"],1,1))
    easyQ.append(Question("Cuantos aminoacidos distintos existen?",
    ["21", "23", "20"],3,1))
    easyQ.append(Question("Donde ocurre la traduccion?",
    ["En la membrana plasmatica", "En el ribosoma", "En la mitocondria"],2,1))
    
    hardQ.append(Question("Cuales son los pasos de la expresión génica?",
    ["Transcripción y traducción", "Transferencia y transcripción", "Traducción y transferencia"],1,2))
    hardQ.append(Question("A que aminoacido corresponde el codigo de 3 letras Gln?",
    ["Glutamina", "Glicina", "Leucina"],1,2))
    hardQ.append(Question("Que nombre reciben las cadenas de aminoacidos?",
    ["Polipeptidos", "Aminopeptidos", "Proteipeptidos"],1,2))
    hardQ.append(Question("Cuantos nucleotidos componen un codon?",
    ["Dos", "Cinco", "Tres"],3,2))
    hardQ.append(Question("Quien se encarga de transferir el codigo genetico en la expresion genica?",
    ["ADN", "Codones", "ARNm"],3,2))
    customPrint('--------------------------------------')
    customPrint(' EL JUEGO DE LA VIDA')
    customPrint('              ')
    customPrint(' Bienvenido al Juego de la Vida. Juego que desafia tus conocimientos sobre la expresion Genica.')
    customPrint(' El juego consiste en una serie de preguntas de las cuales las mas sencillas dan 1 punto, y las mas dificiles 2.')
    customPrint(' Responde correctamente la mayor cantidad de preguntas para obtener el mayor puntaje posible!!!!')
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
    stepOne()
    customPrint(' ')
    stepTwo()
    customPrint(' ')
    showScore()
except:
    customPrint('')





