from fpdf import FPDF
from modules.save_csv import get_data
import os

class PDF(FPDF):
    def header(self):
        self.image('images/logo.png',10,10,30,30)
        self.image('images/header.png',80,20,10,10)
        self.image('images/header.png',(80+50),20,10,10)
        self.image('images/header.png',180,20,10,10)
        self.image('images/body.png',110,30,200)
            
    def footer(self):
        self.set_y(-15)
        self.set_font('Courier', 'B', 8)
        self.cell(0, 10,str(self.page_no()), 0, 0, 'C')

def save(msj,msjRuta):
    distFolder = os.getcwd().replace("\\",'/') + "/Dist"
    datos = get_data()

    # Inicializo la clase
    pdf = PDF()

    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times','',12)

    pdf.set_xy(30,50)
    for i in datos[0]:
        pdf.cell(30,10,i,1,align='C')

    count = 0
    py = 60
    pdf.set_xy(30,60)
    for i in range(1,len(datos)):
        nombre = datos[i][1]
        cn = 0
        aux = ""
        for n in nombre:
            if cn >= 15:
                break
            aux = aux + n
            cn = cn +1
        datos[i][1] = aux
        pdf.set_xy(30,py+(count*10))
        count = count +1

        for j in datos[i]:
            pdf.cell(30,10,j,1,align='C')

        if (count % 20 == 0):
            pdf.add_page()
            count = 0
        
    if (not os.path.exists(distFolder)):
        os.makedirs(distFolder)
    pdf.output('Dist/Datos.pdf','F')
    msj.config(text=f"Guardado con exito.") #
    msjRuta.config(text=f"Ruta almacenada: {distFolder}Dist/Datos.pdf")