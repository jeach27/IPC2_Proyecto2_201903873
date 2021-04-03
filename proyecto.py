import tkinter
from tkinter import *
from tkinter import filedialog 
from tkinter import messagebox
import sys
from xml.dom import minidom
import matriz
import lista


j = None
archivo = None
listaMatrices = lista.lista()

def CargarArchivo():
    j = filedialog.askopenfilename(title = 'Cargar Archivo', filetypes = (('xml files','*.xml'),('all files','*.')))
    archivo = minidom.parse(j)
    matrizz = archivo.getElementsByTagName('matriz')
    for mat in matrizz:
        nombre = mat.getElementsByTagName('nombre')[0]
        filas = mat.getElementsByTagName('filas')[0]
        columnas = mat.getElementsByTagName('columnas')[0]
        imagen = mat.getElementsByTagName('imagen')[0]
        name = nombre.firstChild.data
        x = int(columnas.firstChild.data)
        y = int(filas.firstChild.data)
        img = imagen.firstChild.data
        m = matriz.Matriz(x, y, name)
        fil = 0
        col = -1
        for i in range(len(img)):
            if img[i]=='-':
                col += 1
            if img[i] == '*':
                col += 1
                m.insertar(col, fil, '*')
            if ord(img[i]) == 10:
                if i != 0:
                    if img[i-1] == '-' or img[i-1] == '*':
                        fil += 1
                        col = -1
        #m.graficar()
        listaMatrices.agregarF(m)
   
def Rotaciónhorizontal():
    pass

def Rotaciónvertical():
    pass

def Transpuestaimagen():
    pass

def Limpiarzona():
    pass

def Agregarlíneahorizontal():
    pass

def Agregarlíneavertical():
    pass

def Agregarrectángulo():
    pass

def Agregartriángulo():
    pass

def union():
    pass

def interseccion():
    pass

def diferencia():
    pass

def diferenciaSimetrica():
    pass

def generarReporte():
    Myframe = Frame(ventana)
   
    Myframe.config(width="300", height="320")
    Myframe.pack()
    Myframe.place(x=70,y=100)

    Imagen=PhotoImage(file="grafo.jpg")
    Label(ventana, image=Imagen).pack()

def informacionEstudiante():
    messagebox.showinfo("Informacion Estudiante", "Joaquin Emmanuel Aldair Coromac Huezo \n 201903873 \n IPC2")

def Documentacion():
    pass

if __name__=='__main__':
    ventana = tkinter.Tk()
    ventana.title("Proyecto 2 201903873")
    ventana.config(bg = "blue")
    ventana.geometry("1300x650")
    
    etiqueta = tkinter.Label(ventana, text = "Proyecto 2 - IPC2", font = "BOUNCY 25", bg = "cyan")
    etiqueta.pack(fill = tkinter.X)

    barraMenu = tkinter.Menu(ventana)
    
    menuArchivo = tkinter.Menu(barraMenu)
    menuArchivo.add_command(label = 'Cargar Archivo' ,command = CargarArchivo )

    menuOperaciones = tkinter.Menu(barraMenu)
    menuOperaciones.add_command(label ='Rotación horizontal de una imagen', command = Rotaciónhorizontal )
    menuOperaciones.add_command(label ='Rotación vertical de una imagen', command = Rotaciónvertical)
    menuOperaciones.add_command(label ='Transpuesta de una imagen', command = Transpuestaimagen)
    menuOperaciones.add_command(label ='Limpiar zona de una imagen', command = Limpiarzona)
    menuOperaciones.add_command(label ='Agregar línea horizontal a una imagen', command = Agregarlíneahorizontal)
    menuOperaciones.add_command(label ='Agregar línea vertical a una imagen', command = Agregarlíneavertical)
    menuOperaciones.add_command(label ='Agregar rectángulo', command = Agregarrectángulo)
    menuOperaciones.add_command(label ='Agregar triángulo rectángulo', command = Agregartriángulo)
    menuOperaciones.add_command(label ='Unión A,B', command = union)
    menuOperaciones.add_command(label ='Intersección A,B', command = interseccion)
    menuOperaciones.add_command(label ='Diferencia A,B', command = diferencia)
    menuOperaciones.add_command(label ='Diferencia simétrica A,B', command = diferenciaSimetrica)

    menuReportes = tkinter.Menu(barraMenu)
    menuReportes.add_command(label = 'GenerarReporte', command = generarReporte)

    menuAyuda = tkinter.Menu(barraMenu)
    menuAyuda.add_command(label = 'InformacionEstudiante' ,command = informacionEstudiante)
    menuAyuda.add_command(label='Documentacion', command = Documentacion)

    barraMenu.add_cascade(label = "Cargar Archivo", menu = menuArchivo)
    barraMenu.add_cascade(label = 'Operaciones', menu = menuOperaciones)
    barraMenu.add_cascade(label = 'Reporte' , menu= menuReportes)
    barraMenu.add_cascade(label = 'Ayuda', menu = menuAyuda)
    ventana.config(menu = barraMenu)
    ventana.mainloop()
