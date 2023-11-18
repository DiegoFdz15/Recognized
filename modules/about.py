import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.icons import Icon
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

def newWindow(ws, hs):
    newWindow = ttk.Toplevel()
    newWindow.geometry(f'660x660+{ws//4}+{hs//4}')
    newWindow.iconbitmap("images/icono.ico")
    newWindow.title("RECOGNIZED | About")
    newWindow.config(background="#F3F3F2")

    ## Styles
    mainSt = ttk.Style()
    mainSt.configure('Frame1.TFrame', 
    background="#D9D9D9"
    )

    TitleStyle = ttk.Style()
    TitleStyle.configure('title.TLabel',
    foreground='black',
    width=30,
    font=("Bahnschrift",20),
    padding=5,
    anchor="center"
    )

    intStyle = ttk.Style()
    intStyle.configure('integrantes.TLabel',
    foreground='black',
    font=("Bahnschrift",12),
    padding=5,
    width=30
    )

    resumen = ttk.Style()
    resumen.configure('resumen.TLabel',
    foreground='black',
    font=("Bahnschrift",12),
    padding=5,
    justify="center"
    )

    colegio = ttk.Style()
    colegio.configure('colegio.TLabel',
    foreground='black',
    font=("Bahnschrift",8),
    padding=5,
    justify="center"
    )

    mainF = ttk.LabelFrame(newWindow, bootstyle="primary", text="ACERCA DE NOSOTROS")
    secF = ttk.Frame(mainF)
    footer = ttk.Frame(mainF)

    ## Labels
    lblTitle = ttk.Label(mainF, text='RECOGNIZED', style='title.TLabel')
    lblColegio = ttk.Label(mainF, text='COLEGIO NACIONAL E.M.D "PROF. ATANASIO RIERA"\nÁREA 1', style='colegio.TLabel')
    lblgit = ttk.Label(footer, text='https://github.com/DiegoFdz15/Recognized', style='colegio.TLabel')
    frNosotros = ttk.Frame(mainF)
    lbl1 = ttk.Label(frNosotros, text="""El objetivo principal alrededor del cual se desenvuelve este proyecto es el\ndesarrollo de un sistema de reconocimiento facial.Entre sus objetivos \nespecíficos se encuentran: realizar una primera aproximación sobre las \ntécnicas de reconocimiento facial existentesen la actualidad, elegir una \naplicación donde pueda ser útil el reconocimiento facial, diseñar y \ndesarrollar un programa en Python que lleve a cabo la función de \nreconocimiento facial, y evaluar el funcionamiento del sistema desarrollado. """, style='resumen.TLabel')
    lbl1.pack()
    
    frIntegrantes = ttk.Frame(mainF)
    lbl2 = ttk.Label(frIntegrantes, text='By:', style='integrantes.TLabel')
    lbl2.pack()
    nombres = ['Bruno Rios','Josias johannsen','Enzo Alvarenga','Alexia Ortiz','Federico Díaz','Diego Fernandez']
    n = 1
    for i in nombres:
        a = ttk.Label(frIntegrantes, text=f"   {n}. {i}", style='integrantes.TLabel')
        a.pack()
        n = n +1

    btnCerrar = ttk.Button(
    master=footer, 
    text='Cerrar',  
    style='TButton',
    command=lambda: newWindow.destroy()
    )
    lblColegio.pack()
    lblTitle.pack()
    frNosotros.pack(fill="both",padx=10,pady=15)
    frIntegrantes.pack(fill="both")
    btnCerrar.pack()
    lblgit.pack()

    mainF.pack()
    secF.pack()
    footer.pack()