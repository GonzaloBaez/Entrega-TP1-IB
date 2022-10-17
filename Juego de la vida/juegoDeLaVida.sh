#!/bin/bash
function ayuda(){
	echo -e "Escribe en la consola ./juegoDeLaVida.sh para empezar el juego!"
	}
	
if [ "$1" != "--help" ] && [ "$1" != "--h" ]
	then
		python3 juegoDeLaVida.py
	else
		ayuda
fi
