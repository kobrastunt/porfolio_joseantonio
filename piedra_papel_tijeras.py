import random
import time
"""
Siéntase libre de utilizar este codigo, modificarlo, copiarlo.

Instrucciones para jugar a este juego: 
1- Primeramente la máquina elegirá una de las 3 opciones con los números que van desde el 1 al 3, ambos inclusive.(1 para piedra, 2 para papel y 3 para tijeras)
2- Cuando la máquina haga su elección (secreta), nos pedirá que nosotros la hagamos, decidiendo cualquier número del 1 al 3, ambos inclusive, en el mismo orden explicado anteriormente.
3- Si ganamos se acabará la partida y finalizará el programa y si perdemos ocurrirá lo mismo.
4- Si empatamos, la partida se volverá a iniciar automáticamente, la máquina volverá a escoger otro número y nosotros otro.
5- El bucle se repetirá hasta que uno de los dos gane la partida.


"""
partida = 1

while partida == 1:
    print("Jugador 1: seleccionará un numero del 1 al 3: ")
    print("1------------> Piedra")
    time.sleep(3)
    print("2------------> Papel")
    time.sleep(3)
    print("3------------> Tijeras")
    v1 = random.randint(1, 3)
    time.sleep(3)
    print("El jugador 1 ya eligió un número aleatorio")
    time.sleep(3)
    print("Jugador 2: selecciona entre: ")
    print("1------------> Piedra")
    time.sleep(3)
    print("2------------> Papel")
    time.sleep(3)
    print("3------------> Tijeras")
    
    while True:
        try:
            v2 = int(input())
            if v2 < 1 or v2 > 3:
                print("Por favor, ingresa un número del 1 al 3.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    if v1 != v2:
        if (v1 == 1 and v2 == 3) or (v1 == 2 and v2 == 1) or (v1 == 3 and v2 == 2):
            print("¡¡¡HAS GANADO!!!,TUVISTE BUENA SUERTE!!!")
            partida = 0
        else:
            if (v2 == 1 and v1 == 3) or (v2 == 2 and v1 == 1) or (v2 == 3 and v1 == 2):
                print("¡¡¡HAS PERDIDO, EL GANADOR FUE LA MÁQUINA!!!")
                partida = 0
    else:
        print("EMPATASTEIS.")

print("¡¡Fin del juego!!")
