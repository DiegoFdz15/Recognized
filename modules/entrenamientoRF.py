import cv2
import os
import numpy as np

dataPath = os.getcwd().replace("\\",'/') + "/Data"

def read_train_data(change_msj):
    try:
        peopleList = os.listdir(dataPath)
    except:
        os.makedirs(dataPath)
        peopleList = os.listdir(dataPath)

    label = 0
    labels = []
    facesData = []

    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        change_msj('Leyendo las imagenes')
        for filename in os.listdir(personPath):
            change_msj('Rostros: ' + nameDir + '/' + filename)
            labels.append(label)
            facesData.append(cv2.imread(personPath+'/'+filename,0))
            image = cv2.imread(personPath+'/'+filename,0)
        label = label + 1
    
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.train(facesData, np.array(labels))
    return face_recognizer

def dir_exists(change_msj):
    if not os.path.exists(os.getcwd().replace("\\",'/') + '/modules/modelos/'):
        os.makedirs(os.getcwd().replace("\\",'/') + '/modules/modelos/')
        change_msj("Creando Carpeta de modelo...")

def write_data(face_recognizer,change_msj):
    face_recognizer.write(os.getcwd().replace("\\",'/') + '/modules/modelos/modeloEigenFace.xml')
    change_msj("Modelo almacenado, reinicia el cliente para establecer los cambios.")