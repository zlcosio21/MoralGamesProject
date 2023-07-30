class Inventario:
    def _init_(self):
        self.inventario = []

    def agregar_videojuego(self, titulo, plataforma, precio, stock, genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.stock = stock
        self.genero = genero

        self.inventario.append(self.titulo)
        print(f"Se ha agregado el videojuego {self.titulo} al inventario")

class CarritoDeCompras:
    pass

class Cliente:
    pass

class Compra:
    def _init_(self, *videojuego_comprado):
        self.videojuego_comprado = videojuego_comprado