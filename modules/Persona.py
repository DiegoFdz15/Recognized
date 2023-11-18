import csv
import os
from datetime import datetime

## id, nombre, descripcion, lastUpdate
class Persona:

    def __init__(self):
        self.folder = os.getcwd().replace("\\",'/') + "/csv_data"
        self.name_file = self.folder + f"/datos_usuarios.csv"
        self.id = 0

        if (not os.path.exists(self.folder)):
            os.makedirs(self.folder)
        if (os.path.exists(self.name_file)):
            self.allData = self.getData()
            self.descripcion = self.allData[1][2]
            self.id = self.allData[1][0]
            self.lastUpdate = f'{self.allData[1][3]},{self.allData[1][4]}'
            self.guardar()
            self.lastUpdate = self.changeLastUpdate()
        else:
            print("Archivo no encontrado, creandolo")
            self.descripcion = "Sin descripcion"
            self.lastUpdate = self.changeLastUpdate()
            self.guardar()

    def setId(self, id2):
        self.id = id2
        self.changeLastUpdate()
    
    def setDesc(self, desc):
        self.descripcion = desc
        self.changeLastUpdate()
        self.guardar()
    
    def changeLastUpdate(self):
        today = datetime.now()
        return f'{today.strftime("%x")},{today.strftime("%X")}'
    
    def guardar(self):
        self.file = open(self.name_file, 'w')
        self.changeLastUpdate()
        query = f'id,nombre,descripcion,fecha,hora\n{self.id},{self.nombre},{self.descripcion.replace(",","")},{self.lastUpdate}'
        self.file.write(query)
        self.file.close()
    
    def getData(self):
        aux = []
        with open(self.name_file.replace("/","\\"),"r") as f:
            spamreader = csv.reader(f, delimiter=',')
            for row in spamreader:
                aux.append(','.join(row).split(","))
            return aux
    
    def getDesc(self):
        return self.descripcion