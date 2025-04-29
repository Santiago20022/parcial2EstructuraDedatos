class Node:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

# a) Inorden: Izquierda - Raíz - Derecha
def inorden_iterativo(raiz):
    stack = []
    actual = raiz
    while stack or actual:
        while actual:
            stack.append(actual)
            actual = actual.izq
        actual = stack.pop()
        print(actual.dato, end=' ')
        actual = actual.der

# b) Postorden: Izquierda - Derecha - Raíz
def postorden_iterativo(raiz):
    if raiz is None:
        return
    stack1 = [raiz]
    stack2 = []
    while stack1:
        nodo = stack1.pop()
        stack2.append(nodo)
        if nodo.izq:
            stack1.append(nodo.izq)
        if nodo.der:
            stack1.append(nodo.der)
    while stack2:
        print(stack2.pop().dato, end=' ')

# c) Preorden: Raíz - Izquierda - Derecha
def preorden_iterativo(raiz):
    if raiz is None:
        return
    stack = [raiz]
    while stack:
        nodo = stack.pop()
        print(nodo.dato, end=' ')
        if nodo.der:
            stack.append(nodo.der)
        if nodo.izq:
            stack.append(nodo.izq)
