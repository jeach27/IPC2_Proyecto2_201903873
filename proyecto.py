from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk


from xml.dom import minidom
import matriz
import lista

import webbrowser
import os
from datetime import datetime


j = None
archivo = None
listaMatrices = lista.lista()
listaReporte = lista.lista()

class Reporte:
    def __init__(self,fecha,hora,nombre,filas,columnas,tipo):
        self.fecha = fecha
        self.hora = hora
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.tipo = tipo

def obtenerFecha():
    now = datetime.now()
    return str(now.day) + '/' + str(now.month) + '/' + str(now.year)

def obtenerHora():
    now = datetime.now()
    return str(now.hour) +':'+ str(now.minute) +':'+ str(now.second)

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
        reporte = Reporte(obtenerFecha(), obtenerHora(), nombre, filas, columnas, "ingresoArchivo")
        listaReporte.agregarF(reporte)
    #listaMatrices.imprimir()
    combo.place(x=70,y=80)
    aux = listaMatrices.head
    lista = list()
    while aux:
        lista.append(aux.data.raiz.codigo)
        aux = aux.next
    combo['values'] = lista   
    combo.current(0)

    combo1.place(x=220,y=80)
    aux = listaMatrices.head
    combo1['values'] = lista   
    combo1.current(0)
    
def Rotaciónhorizontal():
    
    matr = combo.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next
    mat = matriz.Matriz(aux.data.columnas, aux.data.filas, aux.data.raiz.codigo)
    for i in range(aux.data.filas):
        auxC = aux.data.buscarFila(i)
        if auxC.derecha != None:
            auxC = auxC.derecha
        for j in range(aux.data.columnas):
            if aux.data.buscarNodo(j, i) == True:
                    mat.insertar(j, aux.data.filas-i-1 , auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha
    mat.graficar()        
    listaReporte.agregarF(Reporte(obtenerFecha(), obtenerHora(), matr, aux.data.filas, aux.data.columnas, 'RotacionHorizontal'))
  
def Rotaciónvertical():
    matr = combo.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next
    mat = matriz.Matriz(aux.data.columnas, aux.data.filas, aux.data.raiz.codigo)
    for i in range(aux.data.filas):
        auxC = aux.data.buscarFila(i)
        if auxC.derecha != None:
            auxC = auxC.derecha
        for j in range(aux.data.columnas):
            if aux.data.buscarNodo(j, i) == True:
                    mat.insertar(aux.data.columnas-j-1, i , auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha
    mat.graficar()
    listaReporte.agregarF(Reporte(obtenerFecha(), obtenerHora(), matr, aux.data.filas, aux.data.columnas, 'RotacionVertical'))

def Transpuestaimagen():
    matr = combo.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next
    mat = matriz.Matriz(aux.data.filas, aux.data.columnas, aux.data.raiz.codigo)
    for i in range(aux.data.filas):
        auxC = aux.data.buscarFila(i)
        if auxC.derecha != None:
            auxC = auxC.derecha
        for j in range(aux.data.columnas):
            if aux.data.buscarNodo(j, i) == True:
                    mat.insertar(i, j , auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha
    mat.graficar()
    listaReporte.agregarF(Reporte(obtenerFecha(), obtenerHora(), matr, aux.data.filas, aux.data.columnas, 'TranspuestaImagen'))

def Limpiarzona():
    x1 = int(input('Ingrese x inicial\n'))
    y1 = int(input('Ingrese y inicial\n'))
    x2 = int(input('Ingrese x final\n'))+1
    y2 = int(input('Ingrese y final\n'))+1
    matr = combo.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next

    mat = matriz.Matriz(aux.data.columnas, aux.data.filas, aux.data.raiz.codigo)
    for i in range(aux.data.filas):
        auxC = aux.data.buscarFila(i)
        if auxC != None:
            if auxC.derecha!=None:
                auxC = auxC.derecha
            for j in range(aux.data.columnas):
                if aux.data.buscarNodo(j, i) != False:
                    mat.insertar(j, i, auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha
    for i in range(x1,x2):
        for j in range(y1,y2):
            if mat.buscarNodo(i, j) != False:
                mat.ReemplazarNodo(i, j, ' ')
    mat.graficar()
    listaReporte.agregarF(Reporte(obtenerFecha(), obtenerHora(), matr, aux.data.filas, aux.data.columnas, 'LimpiarZona'))

def Agregarlíneahorizontal():
    x1 = int(input('Ingrese x inicial\n'))
    y1 = int(input('Ingrese y inicial\n'))
    xn = int(input('Ingrese longitud de linea\n'))
    matr = combo.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next

    mat = matriz.Matriz(aux.data.columnas, aux.data.filas, aux.data.raiz.codigo)
    for i in range(aux.data.filas):
        auxC = aux.data.buscarFila(i)
        if auxC != None:
            if auxC.derecha!=None:
                auxC = auxC.derecha
            for j in range(aux.data.columnas):
                if aux.data.buscarNodo(j, i) != False:
                    mat.insertar(j, i, auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha
    for i in range(xn):
        if mat.buscarNodo(x1, y1) != True:
            mat.insertar(x1, y1, '*')
        x1 += 1
    mat.graficar() 
    listaReporte.agregarF(Reporte(obtenerFecha(), obtenerHora(), matr, aux.data.filas, aux.data.columnas, 'AgregarLineaHorizontal'))         

def Agregarlíneavertical():
    x1 = int(input('Ingrese x inicial\n'))
    y1 = int(input('Ingrese y inicial\n'))
    xn = int(input('Ingrese longitud de linea\n'))
    matr = combo.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next

    mat = matriz.Matriz(aux.data.columnas, aux.data.filas, aux.data.raiz.codigo)
    for i in range(aux.data.filas):
        auxC = aux.data.buscarFila(i)
        if auxC != None:
            if auxC.derecha!=None:
                auxC = auxC.derecha
            for j in range(aux.data.columnas):
                if aux.data.buscarNodo(j, i) != False:
                    mat.insertar(j, i, auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha
    for _ in range(xn):
        if mat.buscarNodo(x1, y1) == False:
            mat.insertar(x1, y1, '*')
        y1 += 1
    mat.graficar() 
    listaReporte.agregarF(Reporte(obtenerFecha(), obtenerHora(), matr, aux.data.filas, aux.data.columnas, 'AgregarLineaVertical'))

def Agregarrectángulo():
    x1 = int(input('Ingrese x inicial\n'))
    y1 = int(input('Ingrese y inicial\n'))
    f = int(input('Ingrese No. filas para rectangulo\n'))
    c = int(input('Ingrese No. columnas para rectangulo\n'))
    matr = combo.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next

    mat = matriz.Matriz(aux.data.columnas, aux.data.filas, aux.data.raiz.codigo)
    for i in range(aux.data.filas):
        auxC = aux.data.buscarFila(i)
        if auxC != None:
            if auxC.derecha!=None:
                auxC = auxC.derecha
            for j in range(aux.data.columnas):
                if aux.data.buscarNodo(j, i) != False:
                    mat.insertar(j, i, auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha

    for _ in range(f-1):
        if mat.buscarNodo(x1, y1) == False:
            mat.insertar(x1, y1, '*')
        y1 += 1
    for _ in range(c-1):
        if mat.buscarNodo(x1, y1) == False:
            mat.insertar(x1, y1, '*')
        x1 += 1
    for _ in range(f-1):
        if mat.buscarNodo(x1, y1) == False:
            mat.insertar(x1, y1, '*')
        y1 -= 1
    for _ in range(c-1):
        if mat.buscarNodo(x1, y1) == False:
            mat.insertar(x1, y1, '*')
        x1 -= 1
    mat.graficar()
    listaReporte.agregarF(Reporte(obtenerFecha(), obtenerHora(), matr, aux.data.filas, aux.data.columnas, 'AgregarRectangulo'))

def Agregartriángulo():
    x1 = int(input('Ingrese x inicial\n'))
    y1 = int(input('Ingrese y inicial\n'))
    l = int(input('Ingrese longitud de catetos\n'))
    matr = combo.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next

    mat = matriz.Matriz(aux.data.columnas, aux.data.filas, aux.data.raiz.codigo)
    for i in range(aux.data.filas):
        auxC = aux.data.buscarFila(i)
        if auxC != None:
            if auxC.derecha!=None:
                auxC = auxC.derecha
            for j in range(aux.data.columnas):
                if aux.data.buscarNodo(j, i) != False:
                    mat.insertar(j, i, auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha
    for _ in range(l-1):
        if mat.buscarNodo(x1, y1) == False:
            mat.insertar(x1, y1, '*')
        y1 += 1
    for _ in range(l-1):
        if mat.buscarNodo(x1, y1) == False:
            mat.insertar(x1, y1, '*')
        x1 += 1
    for _ in range(l-1):
        if mat.buscarNodo(x1, y1) == False:
            mat.insertar(x1, y1, '*')
        x1 -= 1
        y1 -= 1
    mat.graficar()
    listaReporte.agregarF(Reporte(obtenerFecha(), obtenerHora(), matr, aux.data.filas, aux.data.columnas, 'AgregarTriangulo'))

def union():
    matr = combo.get()
    matr2 = combo1.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next
    aux2 = listaMatrices.head
    while aux2:
        if matr2 == aux2.data.raiz.codigo:
            break
        else:
            aux2 = aux2.next
    filas1 = aux.data.filas
    columnas1 = aux.data.columnas
    filas2 = aux2.data.filas
    columnas2 = aux2.data.columnas
    filasF = 0
    columnasF = 0
    if filas1 >= filas2:
        filasF = filas1
    if filas1 <= filas2:
        filasF = filas2
    if columnas1 >= columnas2:
        columnasF = columnas1
    if columnas1 <= columnas2:
        columnasF = columnas2
    mat = matriz.Matriz(columnasF, filasF, 'RU')

    for i in range(filas1):
        auxC = aux.data.buscarFila(i)
        if auxC != None:
            if auxC.derecha!=None:
                auxC = auxC.derecha
            for j in range(columnas1):
                if aux.data.buscarNodo(j, i) == True:
                    mat.insertar(j, i, auxC.codigo)  
                    if auxC.derecha != None:
                        auxC = auxC.derecha 
    for h in range(filas2):
        auxC1 = aux2.data.buscarFila(h)
        if auxC1 != None:
            if auxC1.derecha!=None:
                auxC1 = auxC1.derecha
            for k in range(columnas2):
                if aux2.data.buscarNodo(k, h) == True:
                    if mat.buscarNodo(k, h) == False:
                        mat.insertar(k, h, auxC1.codigo)  
                    if auxC1.derecha != None:
                        auxC1 = auxC1.derecha
    mat.graficar()

    listaReporte.agregarF(Reporte(obtenerFecha(),obtenerHora(),aux.data.raiz.codigo+' '+aux2.data.raiz.codigo,'No Aplica','No Aplica','Union'))

def interseccion():
    matr = combo.get()
    matr2 = combo1.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next
    aux2 = listaMatrices.head
    while aux2:
        if matr2 == aux2.data.raiz.codigo:
            break
        else:
            aux2 = aux2.next
    filas1 = aux.data.filas
    columnas1 = aux.data.columnas
    filas2 = aux2.data.filas
    columnas2 = aux2.data.columnas
    filasF = 0
    columnasF = 0
    if filas1 >= filas2:
        filasF = filas1
    if filas1 <= filas2:
        filasF = filas2
    if columnas1 >= columnas2:
        columnasF = columnas1
    if columnas1 <= columnas2:
        columnasF = columnas2
    mat = matriz.Matriz(columnasF, filasF, 'RI')
    for i in range(filas1):
        auxC = aux.data.buscarFila(i)
        if auxC != None:
            if auxC.derecha!=None:
                auxC = auxC.derecha
            for j in range(columnas1):
                if aux.data.buscarNodo(j, i) == True:
                    if aux2.data.buscarNodo(j, i) == True:
                        mat.insertar(j, i, auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha 

    for h in range(filas2):
        auxC1 = aux2.data.buscarFila(h)
        if auxC1 != None:
            if auxC1.derecha!=None:
                auxC1 = auxC1.derecha
            for k in range(columnas2):
                if aux2.data.buscarNodo(k, h) == True:
                    if aux.data.buscarNodo(k, h) == True:
                        if mat.buscarNodo(k, h) == False:
                            mat.insertar(k, h, auxC1.codigo)  
                    if auxC1.derecha != None:
                        auxC1 = auxC1.derecha
    
    mat.graficar()
    listaReporte.agregarF(Reporte(obtenerFecha(),obtenerHora(),aux.data.raiz.codigo+' '+aux2.data.raiz.codigo,'No Aplica','No Aplica','Interseccion'))

def diferencia():
    matr = combo.get()
    matr2 = combo1.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next
    aux2 = listaMatrices.head
    while aux2:
        if matr2 == aux2.data.raiz.codigo:
            break
        else:
            aux2 = aux2.next
    filas1 = aux.data.filas
    columnas1 = aux.data.columnas
    mat = matriz.Matriz(columnas1, filas1, 'RD')
    for i in range(filas1):
        auxC = aux.data.buscarFila(i)
        if auxC != None:
            if auxC.derecha!=None:
                auxC = auxC.derecha
            for j in range(columnas1):
                if aux.data.buscarNodo(j, i) == True:
                    if aux2.data.buscarNodo(j, i) == False:
                        mat.insertar(j, i, auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha
    mat.graficar()
    listaReporte.agregarF(Reporte(obtenerFecha(),obtenerHora(),aux.data.raiz.codigo+' '+aux2.data.raiz.codigo,'No Aplica','No Aplica','Diferencia'))

def diferenciaSimetrica():
    matr = combo.get()
    matr2 = combo1.get()
    aux = listaMatrices.head
    while aux:
        if matr == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next
    aux2 = listaMatrices.head
    while aux2:
        if matr2 == aux2.data.raiz.codigo:
            break
        else:
            aux2 = aux2.next
    filas1 = aux.data.filas
    columnas1 = aux.data.columnas
    filas2 = aux2.data.filas
    columnas2 = aux2.data.columnas
    filasF = 0
    columnasF = 0
    if filas1 >= filas2:
        filasF = filas1
    if filas1 <= filas2:
        filasF = filas2
    if columnas1 >= columnas2:
        columnasF = columnas1
    if columnas1 <= columnas2:
        columnasF = columnas2
    mat = matriz.Matriz(columnasF, filasF, 'RDS')
    for i in range(filas1):
        auxC = aux.data.buscarFila(i)
        if auxC != None:
            if auxC.derecha!=None:
                auxC = auxC.derecha
            for j in range(columnas1):
                if aux.data.buscarNodo(j, i) == True:
                    if aux2.data.buscarNodo(j, i) == False:
                        mat.insertar(j, i, auxC.codigo)
                    if auxC.derecha != None:
                        auxC = auxC.derecha 

    for h in range(filas2):
        auxC1 = aux2.data.buscarFila(h)
        if auxC1 != None:
            if auxC1.derecha!=None:
                auxC1 = auxC1.derecha
            for k in range(columnas2):
                if aux2.data.buscarNodo(k, h) == True:
                    if aux.data.buscarNodo(k, h) == False:
                        if mat.buscarNodo(k, h) == False:
                            mat.insertar(k, h, auxC1.codigo)  
                    if auxC1.derecha != None:
                        auxC1 = auxC1.derecha
    
    mat.graficar()
    listaReporte.agregarF(Reporte(obtenerFecha(),obtenerHora(),aux.data.raiz.codigo+' '+aux2.data.raiz.codigo,'No Aplica','No Aplica','DiferenciaSimetrica'))

def generarReporte():
    f = open('reporte.html','w')
    f.write('<html>\n')
    f.write('   <head>\n')
    f.write(' <title>Tabla Reporte</title>\n')
    f.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n')
    f.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css">\n')
    f.write('<script src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>\n')
    f.write('   </head>\n')
    f.write('   <body>\n')
    f.write('       <table class="table table-striped table-dark">\n')
    f.write('       <thead>\n')
    f.write('           <tr>\n')
    f.write('               <th scope="col">No</th>\n')   
    f.write('               <th scope="col">Fecha</th>\n')
    f.write('               <th scope="col">Hora</th>\n')
    f.write('               <th scope="col">Nombre</th>\n')
    f.write('               <th scope="col">Filas</th>\n')
    f.write('               <th scope="col">Columnas</th>\n')
    f.write('               <th scope="col">Tipo</th>\n')
    f.write('           </tr>\n')
    f.write('       </thead>\n')
    f.write('       <tbody>\n')
    
    j = listaReporte.head
    for e in range(listaReporte.size):

        f.write('           <tr>\n')
        f.write('               <th scope="row">'+str(e+1)+'</th>\n')
        f.write('               <td>'+str(j.data.fecha)+'</td>\n')
        f.write('               <td>'+str(j.data.hora)+'</td>\n')
        f.write('               <td>'+str(j.data.nombre)+'</td>\n')
        f.write('               <td>'+str(j.data.filas)+'</td>\n')
        f.write('               <td>'+str(j.data.columnas)+'</td>\n')
        f.write('               <td>'+str(j.data.tipo)+'</td>\n')
        f.write('           </tr>\n')
        if j.next != None:
            j = j.next
        
    f.write('       </tbody>\n')
    f.write('       </table>\n')
    f.write('   </body>\n')
    f.write('</html>\n')
    
    f.close()

    webbrowser.open_new_tab('reporte.html')

def informacionEstudiante():
    messagebox.showinfo("Informacion Estudiante", ">Joaquin Emmanuel Aldair Coromac Huezo \n>201903873 \n>Introducion a la Programacion y Computacion 2\n>Ingenieria en Ciencias y Sistemas\n>5to Semestre")

def Documentacion():
    pass

if __name__=='__main__':
    ventana = Tk()
    ventana.title("Proyecto 2 201903873")
    ventana.config(bg = "blue")
    ventana.geometry("1000x650")
    
    etiqueta = Label(ventana, text = "Proyecto 2 - IPC2")
    etiqueta.pack(fill = X)

    barraMenu = Menu(ventana)
    
    menuArchivo = Menu(barraMenu)
    menuArchivo.add_command(label = 'Cargar Archivo' ,command = CargarArchivo )

    menuOperaciones = Menu(barraMenu)
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

    menuReportes = Menu(barraMenu)
    menuReportes.add_command(label = 'GenerarReporte', command = generarReporte)

    menuAyuda = Menu(barraMenu)
    menuAyuda.add_command(label = 'InformacionEstudiante' ,command = informacionEstudiante)
    menuAyuda.add_command(label='Documentacion', command = Documentacion)

    barraMenu.add_cascade(label = "Cargar Archivo", menu = menuArchivo)
    barraMenu.add_cascade(label = 'Operaciones', menu = menuOperaciones)
    barraMenu.add_cascade(label = 'Reporte' , menu= menuReportes)
    barraMenu.add_cascade(label = 'Ayuda', menu = menuAyuda)
    ventana.config(menu = barraMenu)
    combo = ttk.Combobox(ventana, state = 'readonly')
    combo1 = ttk.Combobox(ventana, state = 'readonly')
    ventana.mainloop()
