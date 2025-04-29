class Nodo:
    def __init__(self, tipo, contenido):
        self.tipo = tipo  # 0 = dato, 1 = subestructura
        self.contenido = contenido
        self.siguiente = None
