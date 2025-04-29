from Arbol import Arbol
from Nodo import Nodo

estructura = Arbol()

estructura.insertar_final(0, "A")

nodo_b = Nodo(0, "B")
nodo_c = Nodo(0, "C")
nodo_b.liga = nodo_c
subestructura = Nodo(1, nodo_b)

estructura.insertar_final(1, subestructura.dato)
estructura.insertar_final(0, "D")

estructura.imprimir()

estructura.insertar_final(0, "E")
estructura.imprimir()

estructura.eliminar_dato("D")
estructura.imprimir()
