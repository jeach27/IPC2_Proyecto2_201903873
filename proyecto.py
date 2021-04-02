import tkinter
from io import open 
from tkinter import scrolledtext as st
from tkinter import filedialog as FileDialog
from tkinter import messagebox
import os.path
import sys


def CargarArchivo():
    archivo = FileDialog.askopenfilename( initialdir='.', title = "Abrir un fichero"  )
    return archivo

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
    text = st.ScrolledText(ventana, width = 90, height = 32)
    text.place(x = 30, y = 90)

    console = st.ScrolledText(ventana, width = 54, height = 32, bg = "black", foreground = "white")
    console.place (x = 820, y = 90)

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
