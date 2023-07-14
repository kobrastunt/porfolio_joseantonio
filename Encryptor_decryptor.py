
def dame_mensaje_en_mayusculas(mensaje):
    return (mensaje.upper())

def encriptar(mensaje,clave):
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
    
modo = input("¿Quieres encriptar(e) o desencriptar(d)? ")

if modo == "e":
    mensaje = input("introduce el mensaje a encriptar: ")
    clave = int(input("introduce la clave: "))
    
    mensaje_encriptado = encriptar(mensaje, clave)
    print(mensaje_encriptado)
else:
    mensaje = input("introduce el mensaje a desencriptar: ")
    clave = int(input("introduce la clave: "))
    mensaje_original = desencriptar(mensaje, clave)
    print(mensaje_original)
