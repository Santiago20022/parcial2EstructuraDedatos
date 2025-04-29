from Nodo import Nodo

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar_final(self, tipo, contenido):
        nuevo_nodo = Nodo(tipo, contenido)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        nodo_actual = self.raiz
        while nodo_actual.liga:
            nodo_actual = nodo_actual.liga
        nodo_actual.liga = nuevo_nodo

    def eliminar_dato(self, valor_a_eliminar):
        nodo_dummy = Nodo(0, None)
        nodo_dummy.liga = self.raiz
        nodo_anterior = nodo_dummy
        nodo_actual = self.raiz

        while nodo_actual:
            if nodo_actual.sw == 0 and nodo_actual.dato == valor_a_eliminar:
                nodo_anterior.liga = nodo_actual.liga
                break
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.liga

        self.raiz = nodo_dummy.liga

    def imprimir(self):
        def _imprimir_recursivo(nodo):
            print("(", end="")
            nodo_actual = nodo
            while nodo_actual:
                if nodo_actual.sw == 0:
                    print(nodo_actual.dato, end="")
                else:
                    _imprimir_recursivo(nodo_actual.dato)
                if nodo_actual.liga:
                    print(", ", end="")
                nodo_actual = nodo_actual.liga
            print(")", end="")

        if self.raiz:
            _imprimir_recursivo(self.raiz)
        else:
            print("()")
