import imutils
import cv2
from PIL import Image
from PIL import ImageTk
import os
from datetime import datetime
from modules.logFace import logFace
from modules.session import *

file = os.getcwd().replace("\\",'/') + "/modules/modelos/modeloEigenFace.xml"

if (os.path.exists(file)):
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face_recognizer.read( os.getcwd().replace("\\",'/') + "/modules/modelos/modeloEigenFace.xml")
else:
    print("Archivo no encontrado")

def visualizar(cap, labelVideo, msj, ws, hs):
    labelVideo.config(background='#F3F3F2')
    dataPath = os.getcwd().replace("\\",'/') + "/Data" ###
    imagePaths = os.listdir(dataPath) ###

    if cap is not None:
        ret, frame = cap.read()
        if ret:
            frame = imutils.resize(frame, width=640)
            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxframe = gray.copy()

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            faces = faceClassif.detectMultiScale(gray, 1.3,5)

            if (len(faces) >= 1):
                i = 0
                for f in faces:
                    isMinor = i < len(imagePaths)
                    face = faces[i]
                    (x,y,w,h) = face
                    rostro = auxframe[y:y+h, x:x+w]
                    rostro = cv2.resize(rostro, (150,150), interpolation=cv2.INTER_CUBIC)
                    result = face_recognizer.predict(rostro)

                    if result[1] < 5000 and isMinor:
                        cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x,y-25),1,1.1,(0, 255, 0),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0),2)
                        cv2.putText(frame, 'Rango: {}'.format(int(result[1])), (x,y-5),1,1.3,(0,255,0),1,cv2.LINE_AA)
                        today = datetime.now()
                        logFace(f'El usuario ha iniciado sesion. {today.strftime("%x")} a las {today.strftime("%X")}.\n', imagePaths[result[0]])
                        labelVideo.config(text=f"Bienvenido, {imagePaths[result[0]]}", style='Inverse.TLabel', font=("Arial",25), padding=10)
                        msj.config(text="Recognized")
                        cap.release()
                        newWindow(ws, hs, imagePaths[result[0]])

                    # elif (isMinor and result[1] < 10000):
                    #     cv2.putText(frame, 'Desconocido, Rostro similar: {}'.format(imagePaths[result[0]]), (x,y-25),1,1.1,(255,127,80),1,cv2.LINE_AA)
                    #     today = datetime.now()
                    #     logFace(f'Un usuario similar a "{imagePaths[result[0]]}" ha intentado iniciar sesion. {today.strftime("%x")} a las {today.strftime("%X")}.\n', imagePaths[result[0]] + "_failed")
                    #     cv2.rectangle(frame, (x,y), (x+w,y+h), (255,127,80),2)
                    #     cv2.putText(frame, 'Rango: {}'.format(int(result[1])), (x,y-5),1,1.3,(255,127,80),1,cv2.LINE_AA)
                    elif (isMinor):
                        cv2.putText(frame, 'Desconocido', (x,y-25),1,1.1,(255, 0, 0),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
                        cv2.putText(frame, 'Rango: {}'.format(int(result[1])), (x,y-5),1,1.3,(255,0,0),1,cv2.LINE_AA)
                    i = i + 1
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            labelVideo.configure(image=img)
            labelVideo.image = img

            labelVideo.after(10, lambda: visualizar(cap, labelVideo, msj, ws, hs))
        else:
            labelVideo.image = ""
            cap.release()