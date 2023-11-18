import cv2
import os
import imutils
from PIL import Image, ImageTk
from pygrabber.dshow_graph import FilterGraph
from modules.save_csv import guardar, get_data 

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
count = 0
n = 100

def preCap(personName, cap, lblvideo, label):
    graph = FilterGraph()
    try:
        if (not graph.get_input_devices()):
            return
    except ValueError:
        label.config(text="Debes tener acceso a la cámara.")
        return
    dataPath = os.getcwd().replace("\\",'/') + "/Data"
    personPath = dataPath + "/" + personName

    temp = get_data()
    if (len(temp) > 1):
        guardar(id=int(temp[-1][0])+1,nombre=personName)
    else:
        guardar(nombre=personName)

    if not os.path.exists(personPath):
        texto = "Creando Carpeta de usuario " + personName
        os.makedirs(personPath)
    else:
        texto = "Usuario {} encontrado.".format(personName)
    
    label.config(text=texto)
    label.update()
    
    capturar(cap, lblvideo, personPath, label)


def capturar(cap, lblvideo, ruta, label):
    global count
    global n
    is_reading, frame = cap.read()

    frame = imutils.resize(frame, width=640)
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxframe = frame.copy()
    faces = faceClassif.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
        rostro = auxframe[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150,150), interpolation=cv2.INTER_CUBIC)
        if (count < n):
            cv2.imwrite(ruta + '/rostro_{}.jpg'.format(count), rostro)
            msjOutput = ruta + '/rostro_{}.jpg'.format(count)
            label.config(text=msjOutput)
            label.update()
            count = count +1
        else:
            label.config(text="Captura completa. | {} rostros capturados.".format(n))
            label.update()

            img = Image.open(os.getcwd().replace('\\','/') + '/images/portada.png')
            img = ImageTk.PhotoImage(img)
            lblvideo.configure(image=img)
            lblvideo.image = img
            cap.release()
            return
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lblvideo.imgtk = imgtk
    lblvideo.configure(image=imgtk)
    lblvideo.after(1,lambda: capturar(cap, lblvideo, ruta, label)) 