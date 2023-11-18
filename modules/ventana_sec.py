from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttk
import os
import cv2
from PIL import Image, ImageTk
from modules.capturar import preCap
from modules.entrenamientoRF import *
from modules.about import newWindow as aboutW
from modules.allUsers import newWindow as usersW

# 0 = nada
pressed = 0

def handlerVerUsuarios(e=None):
    usersW(ws,hs)

def handlerAbout(e=None):
    aboutW(ws,hs)

def ventanaSec(ws,hs):
    cap = cv2.VideoCapture(0)

    barra_menus = ttk.Menu()

    ver = tk.Menu(barra_menus, tearoff=False)
    about = tk.Menu(barra_menus, tearoff=False)
    archivo = tk.Menu(barra_menus, tearoff=False)

    about.add_command(
        label="Acerca de",
        accelerator="Ctrl+a",
        command=handlerAbout
    )

    ver.add_command(
        label="Ver Usuarios",
        accelerator="Ctrl+v",
        command=handlerVerUsuarios
    )
    archivo.add_separator()
    archivo.add_command(
        label="Salir",
        command=lambda: root.destroy()
    )

    barra_menus.add_cascade(menu=archivo, label="Archivo")
    barra_menus.add_cascade(menu=ver, label="Ver")
    barra_menus.add_cascade(menu=about, label="Ayuda")

    def handler(num_handler, label, nombre=None, lblVideo=None):
        global pressed
        if (num_handler == 1 and (pressed == 0 or pressed == 1)):
            pressed = 1
            handler_cap(label, nombre, lblVideo)

            pressed = 0
        elif (num_handler == 2 and (pressed == 0 or pressed == 2)):
            pressed = 2
            handler_train()
            pressed = 0

    def handler_cap(label, nombre, lblVideo):
        global name
        name = nombre
        if nombre == "" or nombre == "Ingresa su nombre":
            change_msj("Debes ingresar un nombre para iniciar la captura.")
            return
        preCap(nombre, cap, lblVideo, label)

    def handler_train():
        dataPath = os.getcwd().replace("\\",'/') + "/Data"
        if not os.path.exists(dataPath):
            os.makedirs(dataPath)
        else:
            peopleList = os.listdir(dataPath)

        if len(os.listdir(dataPath)) < 1:
            return

        face_r = read_train_data(change_msj)

        dir_exists(change_msj)
        write_data(face_r,change_msj)

    def change_msj(texto):
        msj.config(text=texto)
        msj.update()

    # Crear una ventana secundaria.
    ventana_secundaria = ttk.Toplevel()
    ventana_secundaria.geometry('660x620+{}+{}'.format(ws//4,hs//4))
    ventana_secundaria.iconbitmap("images/icono.ico")

    ventana_secundaria.config(menu=barra_menus, background="#F3F3F2")
    ventana_secundaria.bind_all("<Control-v>", handlerVerUsuarios)
    ventana_secundaria.bind_all("<Control-V>", handlerVerUsuarios)
    ventana_secundaria.bind_all("<Control-a>", handlerAbout)
    ventana_secundaria.bind_all("<Control-A>", handlerAbout)

    ventana_secundaria.title("RECOGNIZED | Registrar Rostro")

    ## Bottones
    buttons_frame = ttk.Frame(master=ventana_secundaria, style='mainFrame.TFrame')

    name_entry = ttk.Entry(master=buttons_frame)
    name_entry.insert(0,'Ingresa su nombre')

    frame_lblVideo = ttk.Frame(master=ventana_secundaria, style='mainFrame.TFrame')
    lblVideo = ttk.Label(master=frame_lblVideo)

    msj_frame = ttk.Frame(master=ventana_secundaria, style='mainFrame.TFrame')
    
    msj = ttk.Label(master=msj_frame, text='Recognized',font='Calibri 12', style="custom.TLabel")

    btnCapturar = ttk.Button(
        master=buttons_frame,
        text="Capturar",
        width=20,
        command=lambda: handler(1, msj, name_entry.get(), lblVideo),
        style='Outline.TButton'
    )
    
    btnEntrenar = ttk.Button(
        master=buttons_frame,
        text="Entrenar",
        width=20,
        command=lambda: handler(2, msj),
        style='Outline.TButton'
    )

    btnCerrar = ttk.Button(
        master=buttons_frame,
        text="Cerrar",
        width=20,
        command=lambda: ventana_secundaria.destroy(),
        style='TButton'
    )

    name_entry.pack(side='left', padx=5, pady=10)
    btnCapturar.pack(side='left', padx=5, pady=10)
    btnEntrenar.pack(side='left', padx=5, pady=10)
    btnCerrar.pack(side='left', padx=5, pady=10)

    ## lbl video
    img = Image.open(os.getcwd().replace('\\','/') + '/images/portada.png')
    img = ImageTk.PhotoImage(img)
    lblVideo.configure(image=img, background='#F3F3F2')
    lblVideo.image = img

    buttons_frame.pack()
    frame_lblVideo.pack()
    lblVideo.pack()
    msj.pack()
    msj_frame.place(x=0,y=560)