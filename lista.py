class nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class lista: 
    def __init__(self):
        self.head = None
        self.size = 0
    
    def vacia(self):
        return self.head == None

    def agregarF(self, data):
        if self.head == None:
            self.head = nodo(data=data)
            self.size += 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = nodo(data=data)
        self.size += 1
   
    def eliminar(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
            self.size -= 1
        elif curr:
            prev.next = curr.next
            curr.next = None
            self.size -= 1

    def UltimoNodo(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    def imprimir( self ):
        node = self.head
        while node != None:
            print(node.data.raiz.codigo)
            node = node.next

