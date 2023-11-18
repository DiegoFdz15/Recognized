########################## IMPORTS
import tkinter as tk
import ttkbootstrap as ttk
import os
import cv2
from pygrabber.dshow_graph import FilterGraph
from modules.ventana_sec import *
from modules.visualizar import visualizar
from modules.about import newWindow as aboutW
from modules.allUsers import newWindow as usersW
import modules.save_csv as svCsv
########################## TKINTER MODULES

def iniciar(msj):
    global cap
    global sl1
    
    graph = FilterGraph()
    try:
        dispositivos = graph.get_input_devices()
    except ValueError:
        msj.config(text="Debes tener acceso a la cámara.")
        return
    
    if (not len(dispositivos) > 0):
        return

    cap = cv2.VideoCapture(0)
    sl1 = ttk.Style()
    lblVideo.config(text="", padding=0, bootstyle='default')
    visualizar(cap, lblVideo, msj, ws, hs)
    sl1.configure('success.Inverse.TLabel', background='#18bc9b', justify="center")

def finalizar():
    global cap
    try:
        sl1.configure('success.Inverse.TLabel', background='white', padding=1, justify="left")
        mensaje.config(text= "Reconocimiento finalizado.")
        cap.release()
        lblVideo.configure(image=img)
        lblVideo.image = img
    except:
        pass

def handlerVerUsuarios(e=None):
    usersW(ws,hs)

def handlerAbout(e=None):
    aboutW(ws,hs)

def fileExistsAndStart():
    file = os.getcwd().replace("\\",'/') + "/modules/modelos/modeloEigenFace.xml"
    if os.path.exists(file):
        mensaje.config(text=f"Archivo encontrado en: {file}")
        iniciar(mensaje)
    else:
        mensaje.config(text= "Archivo no encontrado")

########################## TKINTER
root = ttk.Window()
svCsv.crear()

############## Root Handler
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
    accelerator="Ctrl+s",
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

############## Root Characteristics
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

############## Root Style
root.title("RECOGNIZED")
root['padx'] = 5
root.geometry('660x600+{}+{}'.format(ws//4,hs//4))
root.resizable(False,False)

root.config(menu=barra_menus, background="#F3F3F2")
root.bind_all("<Control-s>", handlerVerUsuarios)
root.bind_all("<Control-S>", handlerVerUsuarios)
root.bind_all("<Control-a>", handlerAbout)
root.bind_all("<Control-A>", handlerAbout)

root.iconbitmap("images/icono.ico")

############## Buttons Functionality

############## Styles
s1 = ttk.Style()
s1.configure('Outline.TButton',
    font=('Calibri',12),
)

s2 = ttk.Style()
s2.configure('TButton',
    font=('Calibri',12),
)
s3 = ttk.Style()
s3.configure("mainFrame.TFrame",
background="#F3F3F2"
)

s4 = ttk.Style()
s4.configure("Inverse.TLabel",
foreground="black"
)

s5 = ttk.Style()
s5.configure("lblvideo.TLabel",
justify="center"
)

main_Frame = ttk.Frame(root)
main_Frame.config(style="mainFrame.TFrame")

btnInciar = ttk.Button(master=main_Frame, text='Iniciar Reconocimiento', command=fileExistsAndStart, style='Outline.TButton')
btnInciar.pack(side='left', padx=5)

btnFin = ttk.Button(master=main_Frame, text='Finalizar Reconocimiento', command=finalizar, style='Outline.TButton')
btnFin.pack(side='left', padx=5)

btnCapturar = ttk.Button(
    master=main_Frame, 
    text='Añadir Rostro', 
    command=lambda: ventanaSec(ws,hs), 
    style='TButton')

btnCapturar.pack(side='left', padx=5)

main_Frame.pack(pady=10)
############## Labels
lblVideo = ttk.Label(root, style='lblvideo.TLabel')

## lbl video
img = Image.open(os.getcwd().replace('\\','/') + '/images/portada.png')
img = ImageTk.PhotoImage(img)
lblVideo.configure(image=img, background='#F3F3F2')
lblVideo.image = img

lblVideo.pack(pady=10)

msjFrame = ttk.Frame(root)

msjS = ttk.Style()
msjS.configure('custom.TLabel',
background="#4582ec",
width=90,
foreground='white',
font=("Arial",10),
padding=5
)

mensaje = ttk.Label(msjFrame, text="Recognized", style="custom.TLabel")
mensaje.pack()
msjFrame.place(x=0,y=560)

############## Main Loop
root.mainloop()