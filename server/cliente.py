#---------------------------------------
# Arduino-Python Ethernet Communication
#---------------------------------------
from socket import *

def enviar(mensaje):
    address = ('192.168.2.55', 5000)
    s = socket(AF_INET, SOCK_DGRAM)

    s.settimeout(1)
    msj = bytes(mensaje, 'utf-8')
    s.sendto(bytes(mensaje, 'utf-8'), address)
    try:
        respuesta, addr = s.recvfrom(2048)
        print(respuesta.decode())
    except:
        print("Error en la transmision")