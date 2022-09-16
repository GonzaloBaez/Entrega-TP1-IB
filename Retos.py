#RETO I: ¿Podés descubrir y anotar el orden en que se ha ejecutado cada operación?
print (((4+5)*2)/5)
# Se ejecuta de izquierda a derecha, primero 4+5, despues el resultado * 2 y despues lo divide por 5

#RETO II: Creá una variable llamada doble, que sea el doble de la suma entre a y b.

a = 5
b = 3

doble = (a + b) * 2

print(doble)

"""RETO III: Digamos que el ADN no es más que un mensaje en clave, que debe ser descifrado o interpretado para 
la síntesis de proteínas. El mensaje está escrito por una secuencia determinada de 4 nucleótidos distintos 
representados por las letras A, T, G y C. Dentro de la célula, el mensaje es transportado por otra 
molécula, el ARN, muy similar al ADN pero con U en vez de T. En este mensaje, cada triplete o grupo de tres 
letras del ARN se denomina codón, y cada aminoácido de las proteínas está codificado por uno o varios codones. 
Así por ejemplo el codón ‘AUG’ codifica para el aminoácido Metionina , el codón ‘AAA’ para Lisina, el codón ‘CUA’ 
para Leucina, etc. ¿Podrías escribir una cadena de ARN que codifique para el péptido (una cadena corta de aminoácidos) 
‘Met-Lis-Lis-Lis-Leu-Leu-Met’ combinando las variables met = ‘AUG’, lis = ‘AAA’ y leu = ‘CUA’ utilizando operadores matemáticos? """

met = 'AUG'
lis = 'AAA'
leu = 'CUA'

print(met + '-' + (lis + '-' ) * 3 + (leu + '-') *2 + met)

""" RETO IV: ¿Cadenas?¿letras? Si hablamos de cadenas y letras en Biología, 
lo primero que se nos viene a la cabeza son las macromoléculas. Como bien sabemos, 
el ADN es un mensaje en clave que guía la síntesis de proteínas. Este mensaje está escrito por 
una secuencia determinada de 4 nucleótidos distintos representados por las letras A, T, G y C. 
El contenido de C y G (es decir el porcentaje de CG) presente en el ADN de un organismo es una característica 
distintiva: por ejemplo las Actinobacterias tienen un contenido característicamente más alto de CG que otros organismos. 
Ahora, contar la cantidad de C y G en una cadena de ADN larguísima a mano puede ser un verdadero tedio ¿Podrías crear un 
programa que calcule el porcentaje de C y G de una cadena dada de ADN? ¡Compartinos tu código en nuestro grupo de Facebook 
‘Talleres de programación Orientada a la Biologia - SBG_UNQ’!Buscanos en Twitter! """

ADN = 'TGATAAGAGTACCCAGAATAAAATGAATAACTTTTTAAAGACAAAATCCTCTGTTATAATATTGCTAAAATTATTCAGAGTAATATTGTGGATTAAAGCCACAATAAGATTTATAATCTTAAATGATGGGACTACCATCCTTACTCTCTCCATTTCAAGGCTGACGATAAGGAGACCTGCTTTGCCGAGGAGGTACTACAGTTCTCTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTGGTGGTTTGTGATTTAGTTGATTTTATAGGCTAGTGGGAGAATTTACATTCAAATGTCTAAATCACTTAAAATTTCCCTTTATGGCCTGACAGTAACTTTTTTTTATTCATTTGGGGACAACTATGTCCGTGAGCTTCCATCCAGAGATTATAGTAGTAAATTGTAATTAAAGGATATGATGCACGTGAAATCACTTTGCAATCAT'
cantidadDeCG = ADN.count('CG')
cantidadDeC = ADN.count('C')
cantidadDeG = ADN.count('G')
cantidadDeLetrasADN = len(ADN)
print('Cadena de ADN: ')
print(ADN)
print('El procentaje de CG en la cadena es de ' + str(cantidadDeCG *100 / cantidadDeLetrasADN) + '%')
print('El procentaje de C en la cadena es de ' + str(cantidadDeC *100 / cantidadDeLetrasADN) + '%')
print('El procentaje de G en la cadena es de ' + str(cantidadDeG *100 / cantidadDeLetrasADN) + '%')

"""RETO V: La Asombrosa Maravillosa es nuestra valiente superheroína. Sus poderes son producto de mutaciones en un gen muy común, 
cuya secuencia en la mayoría de las personas es 'ATGGAACTTGCAATCGAAGTTGGC'. A diferencia de nosotros, el gen mutado de la 
Asombrosa Maravillosa incluye la secuencia 'GTTTGTGGTTG' en su interior. La Asombrosa Maravillosa adquirió sus poderes al 
beber Jugo Vencido. El primer sorbo de esta poción prohibida causa el cambio de todas las citosinas (C) por timinas (T). 
El siguiente sorbo cambia todas las adeninas (A) por guaninas (G). El tercer sorbo cambia las citosinas (C) por adeninas (A). 
El cuarto sorbo... puede ser mortal. ¿Podés escribir un programa que nos diga cuántos sorbos de Jugo Vencido debe beber un portador 
del gen normal, para ganar los poderes de la Asombrosa Maravillosa? ¡Compartinos tu código en nuestro grupo de Facebook ‘Talleres 
de programación Orientada a la Biologia - SBG_UNQ’! Buscanos en Twitter! """

portadorGenNormal = 'ATGGAACTTGCAATCGAAGTTGGC'
sorbosJugoVencidoATomar = []
sorbosJugoVencidoATomar.append('C' in portadorGenNormal)
sorbosJugoVencidoATomar.append('A' in portadorGenNormal)

print('Tiene que tomar '+ str(sorbosJugoVencidoATomar.count(True)) + ' sorbos')
