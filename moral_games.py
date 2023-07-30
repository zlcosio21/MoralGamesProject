class Inventario:
    def __init__(self):
        self.videojuegos = []
        self.genero_videojuegos = {}

    def agregar_videojuego(self, titulo, plataforma, precio, stock, genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.stock = stock
        self.genero = genero 

        print(f"Se ha agregado el videojuego {self.titulo} al inventario")
        self.videojuegos.append(titulo)

        if self.genero in self.genero_videojuegos:
            self.genero_videojuegos[self.genero].append(titulo)
        else:
            self.genero_videojuegos[self.genero] = [titulo]

    def buscar_videojuego(self, videojuego_genero):
        print(f"Se busco {videojuego_genero}, se encontro: ")

        if videojuego_genero in self.genero_videojuegos:
            lista_generos = self.genero_videojuegos[videojuego_genero]
            for videojuego in lista_generos:
                print(f"-{videojuego}")            
        elif videojuego_genero in self.videojuegos:
            print(f"-{videojuego_genero}")
        else:
            print(f"El videojuego o genero, no se encuentra en el inventario")

    def mostrar_videojuegos(self):
        if self.videojuegos:
            print("Los videojuegos que se encuentran en la tienda son:")
            for videojuego in self.videojuegos:
                print(f"-{videojuego}")
        else:
            print("No hay videojuegos en el inventario de la tienda")

class CarritoDeCompras:
    pass

class Cliente:
    pass

class Compra:
    def _init_(self, *videojuego_comprado):
        self.videojuego_comprado = videojuego_comprado