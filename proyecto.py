from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk


from xml.dom import minidom
import matriz
import lista


j = None
archivo = None
listaMatrices = lista.lista()
listaReporte = lista.lista()

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
    matriz = combo.get()
    aux = listaMatrices.head
    while aux:
        if matriz == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next
  
def Rotaciónvertical():
    matriz = combo.get()
    aux = listaMatrices.head
    while aux:
        if matriz == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next

def Transpuestaimagen():
    matriz = combo.get()
    aux = listaMatrices.head
    while aux:
        if matriz == aux.data.raiz.codigo:
            break
        else:
            aux = aux.next

def Limpiarzona():
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
    mat.graficar()

def Agregarlíneahorizontal():
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
    mat.graficar()

def Agregarlíneavertical():
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
    mat.graficar()

def Agregarrectángulo():
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
    mat.graficar()

def Agregartriángulo():
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
    mat.graficar()

def union():
    pass

def interseccion():
    pass

def diferencia():
    pass

def diferenciaSimetrica():
    pass

def generarReporte():
    
    render = PhotoImage(file = 'grafo.gif')
    mens = Label(ventana, image = render).place(x=90,y=90)

def informacionEstudiante():
    messagebox.showinfo("Informacion Estudiante", "Joaquin Emmanuel Aldair Coromac Huezo \n 201903873 \n IPC2")

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
