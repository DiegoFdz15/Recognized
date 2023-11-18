import csv
import os
from datetime import datetime

folder = os.getcwd().replace("\\",'/') + "/csv_data"
name_file = folder + f"/datos_usuarios.csv"

def crear():
    if (not os.path.exists(folder)):
        print("Creando carpeta.")
        os.makedirs(folder)
    if (os.path.exists(name_file)):
        print("Archivo existente")
        return
    f = open(name_file, 'w')
    f.write('id,nombre,descripcion,fecha,hora\n')
    f.close()

def guardar(id=0,nombre="",rol="Sin Rol",fecha="Fecha no registrada",hora="Horario no registrado"):
    f = open(name_file, 'a')
    today = datetime.now()
    fecha = today.strftime("%x")
    hora = today.strftime("%X")
    f.write(f'{id},{nombre},{rol},{fecha},{hora}\n')
    f.close()

def get_data():
    aux = []
    with open(name_file.replace("/","\\"),"r") as f:
        spamreader = csv.reader(f, delimiter=',')
        for row in spamreader:
            aux.append(','.join(row).split(","))
        return aux

def get_data_by_name(nombre):
    temp = get_data()
    for i in temp:
        if (i[1] == nombre):
            return i
    return "No ha sido encontrado."

def borrar():
    os.remove(name_file)

def get_data_and_update(nombre, rol):
    rol = rol.replace("\n","")
    temp = get_data()
    borrar()
    crear()
    for i in range(1,len(temp)):
        if (nombre == temp[i][1]):
            guardar(id=temp[i][0],nombre=temp[i][1],rol=rol,fecha=temp[i][3],hora=temp[i][4])
            print("actualizado con exito.")
        else:
            guardar(id=temp[i][0],nombre=temp[i][1],rol=temp[i][2],fecha=temp[i][3],hora=temp[i][4])