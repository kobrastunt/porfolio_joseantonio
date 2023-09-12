def dame_mensaje_en_mayusculas(mensaje):
    return mensaje.upper() # Esta función nos convierte el mensaje a mayusculas para evitar problemas

"""

La siguiente función toma dos argumentos, el primero realizará la incriptación del mensaje y el siguiente argumento nos 
realizará un desplazamiento según el número indicado.

"""

def encriptar(mensaje, clave):
    mensaje = dame_mensaje_en_mayusculas(mensaje)
    mensaje_encriptado = ''
    for symbol in mensaje:
        if symbol.isalpha():
            num = ord(symbol)
            num += clave
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            
            mensaje_encriptado += chr(num)
        else:
            mensaje_encriptado += str(symbol)
    return mensaje_encriptado

def desencriptar(mensaje, clave):
    return encriptar(mensaje, -clave)

modo = input("¿Quieres encriptar(e) o desencriptar(d)? ").lower()  # convertimos a minúsculas para ser insensible a mayúsculas/minúsculas

# En siguiente bucle nos aseguramos que elijamos lo que se nos pide en el input un valor ("e")encriptar o ("d")desencriptar

while modo not in ["e", "d"]:
    print("Por favor, ingresa 'e' para encriptar o 'd' para desencriptar.")
    modo = input("¿Quieres encriptar(e) o desencriptar(d)? ").lower()

if modo == "e":
    mensaje = input("Introduce el mensaje a encriptar: ")
    clave = int(input("Introduce la clave: "))
    
    mensaje_encriptado = encriptar(mensaje, clave)
    print("Mensaje encriptado:", mensaje_encriptado)
else:
    mensaje = input("Introduce el mensaje a desencriptar: ")
    clave = int(input("Introduce la clave: "))
    mensaje_original = desencriptar(mensaje, clave)
    print("Mensaje desencriptado:", mensaje_original)
