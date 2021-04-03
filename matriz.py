import os

class Nodo:
    def __init__(self,x,y,codigo):
        self.x = x
        self.y = y
        self.codigo = codigo
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None

class Matriz:
    def insertarNodoColumna(self,headC,nuevo):
        aux = headC
        flagC = False

        while True:
            if aux.x > nuevo.x:
                flagC = True
                break
            if aux.derecha != None:
                aux = aux.derecha
            else:
                break
        
        if flagC == True:
            nuevo.derecha = aux
            aux.izquierda.derecha = nuevo
            nuevo.izquierda = aux.izquierda
            aux.izquierda = nuevo
        else:
            aux.derecha = nuevo
            nuevo.izquierda = aux
        
        return nuevo

    def insertarNodoFila(self,headF,nuevo):
        aux = headF
        flagF = False

        while True:
            if aux.y > nuevo.y:
                flagF = True
                break
            if aux.abajo != None:
                aux = aux.abajo
            else:
                break

        if flagF == True:
            nuevo.abajo = aux
            aux.arriba.abajo = nuevo
            nuevo.arriba = aux.arriba
            aux.arriba = nuevo
        else:
            aux.abajo = nuevo
            nuevo.arriba = aux

        return nuevo

    def crearCabeceras(self, columnas,filas ):
        head = self.raiz
        for i in range(columnas):
            newC = Nodo(i, -1, str(i))
            colu = Matriz.insertarNodoColumna(self, head, newC)
        for j in range(filas):
            newF = Nodo(-1, j, str(j))
            fil = Matriz.insertarNodoFila(self, head, newF)

    def __init__(self , columnas,filas  , nombre):
        self.raiz = Nodo(-1, -1, nombre)
        self.columnas = columnas
        self.filas = filas
        Matriz.crearCabeceras(self, columnas,filas )
        
    def buscarColumna(self, x):
        aux = self.raiz
        for i in range(self.columnas+1):
            if aux.x == x:
                return aux
            elif aux.derecha != None:
                aux = aux.derecha
        return None

    def buscarFila(self, y):
        aux = self.raiz
        for i in range(self.filas+1):
            if aux.y == y:
                return aux
            elif aux.abajo != None:
                aux = aux.abajo
        return None

    def insertar(self, x, y ,codigo):
        if x < self.columnas and y < self.filas:
            nuevo = Nodo(x, y, codigo)
            col = Matriz.buscarColumna(self, x)
            fil = Matriz.buscarFila(self, y)
            if col != None and fil != None:
                nuevo = Matriz.insertarNodoFila(self, col, nuevo)
                nuevo  = Matriz.insertarNodoColumna(self, fil, nuevo)
                
        else:
            print('La ubicacion esta fuera de rango')

    def imprimircabecerasColumnas(self):
        aux = self.raiz
        for i in range(self.columnas+1):
            print(aux.codigo+'->')
            if aux.derecha != None:
                aux = aux.derecha
            else:
                break
            
    def imprimircabecerasFilas(self):
        aux = self.raiz
        for i in range(self.filas+1):
            print(aux.codigo+'->')
            if aux.abajo != None:
                aux = aux.abajo
            else:
                break

    def graficar(self):

        file = open('grafo.dot','w')
        file.write('digraph G{\n')

        file.write('graph [pad="0.5", nodesep="0.5", ranksep="2"];\n  node [shape=plain]\n  rankdir=LR; \nFoo [label=< \n<table border="0" cellborder="1" cellspacing="0">\n')
        
        
        
        for i in range(-1,self.filas):
            file.write('<tr>\n')
            auxC = Matriz.buscarFila(self, i)
            if auxC != None:
                for j in range(-1,self.columnas):
                    if auxC.x == j and auxC.y == i:
                        file.write('<td>'+auxC.codigo+'</td>\n')
                        if auxC.derecha != None:
                            auxC = auxC.derecha
                    else:
                        file.write('<td>'+' '+'</td>\n')
            file.write('</tr>\n')
            
            
        file.write('</table>>];\n')
        
        file.write('}')
        file.close() 
        os.system('dot -Tpng grafo.dot -o grafo.jpg')
        os.startfile('grafo.jpg')


 