class Inventario:
    genero_videojuegos = {}
    juegos_inventario = []

    def buscar_videojuego(self, videojuego_genero):
        print(f"Se busco '{videojuego_genero}', se encontro: ")

        if videojuego_genero in self.genero_videojuegos:
            lista_generos = self.genero_videojuegos[videojuego_genero]
            for videojuego in lista_generos:
                print(f"-{videojuego}")            
        elif videojuego_genero in self.juegos_inventario:
            print(f"-{videojuego_genero}")
        else:
            print(f"El videojuego o genero, no se encuentra en el inventario")

    def mostrar_videojuegos(self):
        if self.juegos_inventario:
            print("Los videojuegos que se encuentran en la tienda son:")
            for juego in self.juegos_inventario:
                print(f"-{juego}") 
        else:
            print("No hay videojuegos en el inventario de la tienda")

class Videojuego(Inventario):
    def __init__(self, titulo, plataforma, precio, stock, *genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.stock = stock  
        self.genero = genero
        
        if self.titulo not in self.juegos_inventario:
            print(f"Se ha agregado el videojuego {self.titulo} al inventario")
            self.juegos_inventario.append(self.titulo)
            for genero in self.genero:
                if genero in self.genero_videojuegos:
                    self.genero_videojuegos[genero].append(titulo)
                else:
                    self.genero_videojuegos[genero] = [titulo]
        else:
            print(f"!El videojuego {self.titulo} ya se encuentra en el inventario")       

class CarritoDeCompras:
    pass


class Cliente:
    pass

class Compra:
    def _init_(self, *videojuego_comprado):
        self.videojuego_comprado = videojuego_comprado