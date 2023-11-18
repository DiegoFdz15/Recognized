import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
from modules.save_csv import get_data_by_name, get_data_and_update
from server.cliente import enviar
import threading

def newWindow(ws, hs, nombre):
    newWindow = ttk.Toplevel()
    newWindow.geometry(f'660x620+{ws//4}+{hs//4}')
    newWindow.iconbitmap("images/icono.ico")
    newWindow.config(background='#F3F3F2')
    newWindow.title(f"RECOGNIZED | Usuario")

    th1 = threading.Thread(target=enviar,args=("1"))
    th1.start()

    def on_closing():
        th2 = threading.Thread(target=enviar,args=("0"))
        th2.start()
        newWindow.destroy()

    newWindow.protocol("WM_DELETE_WINDOW", on_closing)

    data = get_data_by_name(nombre)

    ## Styles
    mainSt = ttk.Style()
    mainSt.configure('Frame1.TFrame', 
    background="#F3F3F2"
    )

    btnSt = ttk.Style()
    btnSt.configure('add.TButton',
    font=("Arial",15),
    width=20
    )

    TitleStyle = ttk.Style()
    TitleStyle.configure('title.TLabel',
    foreground='black',
    width=30,
    font=("Bahnschrift",20),
    padding=5,
    anchor="center"
    )

    nameStyle = ttk.Style()
    nameStyle.configure('name.TLabel',
    foreground='#4582ec',
    font=("Arial",15),
    padding=5,
    )

    idStyle = ttk.Style()
    idStyle.configure('id.TLabel',
    foreground='#4582ec',
    font=("Arial",10),
    padding=5,
    )

    descStyle = ttk.Style()
    descStyle.configure('desc.TFrame',
    foreground='#4582ec',
    font=("Arial",15),
    padding=5,
    width=20
    )

    def handlerDesc(description):
        descripcion = description.replace("\n"," ")
        descripcion = description.replace(",",";")
        get_data_and_update(nombre, descripcion)
    
    mainS = ttk.Style()
    mainS.configure('mainFrame.TLabelframe',
    background="#F3F3F2",
    bordercolor='blue'
    )

    mainF = ttk.LabelFrame(newWindow, bootstyle="primary", text="CUENTA")
    secF = ttk.Frame(mainF)
    footer = ttk.Frame(mainF)

    ## Labels
    lblTitle = ttk.Label(mainF, text='RECOGNIZED', style='title.TLabel')
    lblname = ttk.Label(secF, text=f"Nombre: {data[1]}", style='name.TLabel')
    lblid = ttk.Label(secF, text=f"ID: # {data[0]}", style='id.TLabel')
    lblDesc = ScrolledText(secF, padding=5, height=10, autohide=True, vbar=False)
    lblfecha = ttk.Label(footer, text=f"Última actualización: {data[3]} | {data[4]}", style='name.TLabel')
    
    btnUpdate = ttk.Button(
    master=footer, 
    text='Actualizar rol',  
    style='add.TButton',
    command=lambda: handlerDesc(lblDesc.get("1.0",END))
    )

    btnCerrar = ttk.Button(
    master=footer, 
    text='Cerrar',  
    style='TButton',
    command=on_closing
    )
    
    lblTitle.pack(pady=20)
    lblname.pack()
    lblid.pack()
    lblDesc.pack()
    lblDesc.insert(END,data[2])

    btnUpdate.pack(pady=10)
    btnCerrar.pack(pady=10)
    lblfecha.pack(pady=10)

    mainF.pack()
    secF.pack()
    footer.pack()
