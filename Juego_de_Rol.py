import random
import time

class Personaje:
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    arma = "Default"
    daño_arma = 0

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, daño_arma):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.daño_arma = daño_arma

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)
        print(self.arma, ":", sep="")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        ataque = self.elegir_ataque()
        arma = self.cambiar_arma()
        self.realizar_ataque(enemigo, ataque, arma)

    def realizar_ataque(self, enemigo, ataque, arma):
        min_daño = self.obtener_min_daño(ataque)
        max_daño = self.obtener_max_daño(ataque)
        daño = random.randint(min_daño, max_daño) + self.daño_arma
        parte_cuerpo = self.fracturar_cuerpo()
        enemigo.vida -= daño
        print(f"¡{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre} con {self.arma}!")
        time.sleep(2)  # Pausa de 2 segundos antes del siguiente ataque
        print(f"¡{enemigo.nombre} ha sufrido una fractura en {parte_cuerpo}!")
        time.sleep(2)  # Pausa de 2 segundos antes del siguiente ataque
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} es {enemigo.vida}.")
        else:
            enemigo.morir()

    def fracturar_cuerpo(self):
        partes_cuerpo = ["brazo", "pierna", "cabeza"]
        parte_cuerpo = partes_cuerpo[self.generar_numero_aleatorio(len(partes_cuerpo))]
        return parte_cuerpo

    def generar_numero_aleatorio(self, maximo):
        return random.randint(0, maximo - 1)

    def cambiar_arma(self):
        armamento = int(input("Elige un arma: (1) vara lacerante, daño 8. (2) tridente mágico, daño 10 "))
        if armamento == 1:
            self.arma = "vara lacerante"
            self.daño_arma = 8
        elif armamento == 2:
            self.arma = "tridente mágico"
            self.daño_arma = 10
        else:
            print("Número de arma incorrecto")
            self.cambiar_arma()

    def elegir_ataque(self):
        opcion = int(input("Elige un ataque: (1) Ataque ligero, (2) Ataque pesado: "))
        if opcion == 1:
            return 0
        elif opcion == 2:
            return 1
        else:
            print("Número de ataque incorrecto")
            return self.elegir_ataque()

    def obtener_min_daño(self, ataque):
        if ataque == 0:  # Ataque ligero
            return self.fuerza + self.daño_arma
        elif ataque == 1:  # Ataque pesado
            return (self.fuerza * 2) + self.daño_arma

    def obtener_max_daño(self, ataque):
        if ataque == 0:  # Ataque ligero
            return (self.fuerza * 2) + self.daño_arma
        elif ataque == 1:  # Ataque pesado
            return (self.fuerza * 3) + self.daño_arma


class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, 0)

    def cambiar_arma(self):
        armamento = int(input("Elige un arma: (1) vara lacerante, daño 8. (2) tridente mágico, daño 10 "))
        if armamento == 1:
            self.arma = "vara lacerante"
            self.daño_arma = 8
        elif armamento == 2:
            self.arma = "tridente mágico"
            self.daño_arma = 10
        else:
            print("Número de arma incorrecto")
            self.cambiar_arma()

    def atributos(self):
        super().atributos()
        print("Arma:", self.arma)

    def elegir_ataque(self):
        opcion = int(input("Elige un ataque: (1) Ataque ligero, (2) Ataque pesado: "))
        if opcion == 1:
            return 0
        elif opcion == 2:
            return 1
        else:
            print("Número de ataque incorrecto")
            return self.elegir_ataque()

    def obtener_min_daño(self, ataque):
        if ataque == 0:  # Ataque ligero
            return self.fuerza + self.daño_arma
        elif ataque == 1:  # Ataque pesado
            return (self.fuerza * 2) + self.daño_arma

    def obtener_max_daño(self, ataque):
        if ataque == 0:  # Ataque ligero
            return (self.fuerza * 2) + self.daño_arma
        elif ataque == 1:  # Ataque pesado
            return (self.fuerza * 3) + self.daño_arma


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, "libro")

    def cambiar_arma(self):
        armamento = int(input("Elige un arma: (1) vara lacerante, daño 8. (2) tridente mágico, daño 10 "))
        if armamento == 1:
            self.arma = "vara lacerante"
            self.daño_arma = 8
        elif armamento == 2:
            self.arma = "tridente mágico"
            self.daño_arma = 10
        else:
            print("Número de arma incorrecto")
            self.cambiar_arma()

    def atributos(self):
        super().atributos()
        print("Arma:", self.arma)

    def elegir_ataque(self):
        opcion = int(input("Elige un ataque: (1) Bola de fuego, (2) Rayo: "))
        if opcion == 1:
            return 0
        elif opcion == 2:
            return 1
        else:
            print("Número de ataque incorrecto")
            return self.elegir_ataque()

    def obtener_min_daño(self, ataque):
        if ataque == 0:  # Bola de fuego
            return self.inteligencia + self.daño_arma
        elif ataque == 1:  # Rayo
            return (self.inteligencia * 2) + self.daño_arma

    def obtener_max_daño(self, ataque):
        if ataque == 0:  # Bola de fuego
            return (self.inteligencia * 2) + self.daño_arma
        elif ataque == 1:  # Rayo
            return (self.inteligencia * 3) + self.daño_arma


personaje_1 = Guerrero("conan", 20, 10, 4, 100)
personaje_2 = Mago("rinoa", 5, 15, 4, 100)


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)

        if not jugador_2.esta_vivo():
            break

        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)

        turno += 1

    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


combate(personaje_1, personaje_2)
