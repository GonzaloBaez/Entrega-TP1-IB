#!/bin/bash
function ayuda(){
	echo -e "EL juego de la vida consiste en una competencia de preguntas contra un Robotito poco amigable."
	echo -e "El que responda correctamente obtendra puntos, y el que mas puntos tenga gana!"
	echo -e "Es necesario tener instalado Python para ejecutar el programa"
	echo -e "Escribe en la consola ./juegoDeLaVida.sh para empezar el juego!"
	}
	
if [ "$1" != "--help" ] && [ "$1" != "--h" ]
	then
		python3 juegoDeLaVida.py
	else
		ayuda
fi
