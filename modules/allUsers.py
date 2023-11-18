import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.icons import Icon
from ttkbootstrap.constants import *
import os
from modules.save_pdf import save
from modules.save_csv import get_data

def newWindow(ws, hs):
    if (os.path.exists(os.getcwd().replace("\\",'/') + "/Data")):
        pass
    else:
        return
    def onsave():
        save(lblUpdate,lblRuta)
    newWindow = ttk.Toplevel()
    newWindow.geometry(f'660x640+{ws//4}+{hs//4}')
    newWindow.iconbitmap("images/icono.ico")
    newWindow.title("RECOGNIZED | Usuarios")
    newWindow.config(background="#F3F3F2")

    dataPath = os.getcwd().replace("\\",'/') + "/Data"
    imagePaths = os.listdir(dataPath)

    ## Styles
    mainSt = ttk.Style()
    mainSt.configure('Frame1.TFrame', 
    background="#D9D9D9"
    )

    nombresSt = ttk.Style()
    nombresSt.configure('names.TLabel', 
    background="#374F79",
    width=35,
    foreground='white',
    padding=5,
    font=("Bahnschrift",12),
    )

    TitleStyle = ttk.Style()
    TitleStyle.configure('title.TLabel',
    foreground='black',
    width=30,
    font=("Bahnschrift",20),
    padding=5,
    anchor="center"
    )

    mainF = ttk.LabelFrame(newWindow, bootstyle="primary", text="Usuarios")
    secF = ttk.Frame(mainF)
    footer = ttk.Frame(mainF)

    ## Labels
    lblTitle = ttk.Label(mainF, text='RECOGNIZED', style='title.TLabel')
    count = 1
    lblUsers = ttk.Label(mainF, text='Usuarios:', style='title.TLabel')
    lblUpdate = ttk.Label(footer, text='', bootstyle="success")
    lblRuta = ttk.Label(footer, text='')

    userData = get_data()

    for i in range(1,len(userData)):

        lbl_f = ttk.Frame(secF)
        if (count < 9):
            lbl = ttk.Label(lbl_f, text=f'{count}.  {userData[i][1]}',style='names.TLabel')
            lbl.pack()
            lbl_f.pack(pady=5)

        if (count == len(imagePaths) and len(imagePaths) >= 10):
            lbl = ttk.Label(lbl_f, text=f'10. Otros {len(imagePaths) - 10} usuarios.',style='names.TLabel')
            lbl.pack()
            lbl_f.pack(pady=5)
        
        
        count = count +1
    
    btnGuardar = ttk.Button(
    master=footer, 
    text='Guardar',  
    style='TButton',
    command=onsave
    )

    btnCerrar = ttk.Button(
    master=footer, 
    text='Cerrar',  
    style='TButton',
    command=lambda: newWindow.destroy()
    )
    
    lblTitle.pack(pady=20)
    lblUsers.pack()
    btnGuardar.pack()
    btnCerrar.pack(pady=10)
    lblUpdate.pack()
    lblRuta.pack()

    mainF.pack()
    secF.pack()
    footer.pack()