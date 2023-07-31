class Inventario:
    genero_videojuegos = {}
    inventario_videojuegos = [] 
    precio_videojuegos = {}
    stock_videojuegos = {}

    def buscar_videojuego(self, videojuego_genero):
        print(f"Se busco '{videojuego_genero}', se encontro: ")

        if videojuego_genero in self.genero_videojuegos:
            lista_generos = self.genero_videojuegos[videojuego_genero]
            for videojuego in lista_generos:
                print(f"-{videojuego}")            
        elif videojuego_genero in self.inventario_videojuegos:
            print(f"-{videojuego_genero}")
        else:
            print(f"El videojuego o genero, no se encuentra en el inventario")

    def mostrar_videojuegos(self):
        if self.inventario_videojuegos:
            print("Los videojuegos que se encuentran en la tienda son:")
            for juego in self.inventario_videojuegos:
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
        
        if self.titulo not in self.inventario_videojuegos:
            print(f"Se ha agregado el videojuego {self.titulo} al inventario")
            self.inventario_videojuegos.append(self.titulo)
            self.precio_videojuegos[self.titulo] = [self.precio]
            self.stock_videojuegos[self.titulo] = [self.stock]            
            for genero in self.genero:
                if genero in self.genero_videojuegos:
                    self.genero_videojuegos[genero].append(self.titulo)
                else:
                    self.genero_videojuegos[genero] = [self.titulo]
        else:
            print(f"!El videojuego {self.titulo} ya se encuentra en el inventario")       

class Cliente(Inventario):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.productos_carrito = []

    def tomar_carrito(self):
        print(f"El Cliente {self.nombre} {self.apellido} a tomado un carrito")

class Compra(Cliente):
    def _init_(self, *videojuego_comprado):
        self.videojuego_comprado = videojuego_comprado