class Inventario:
    genero_videojuegos = {}
    inventario_videojuegos = [] 
    precio_videojuegos = {}
    stock_videojuegos = {}
    requisitos_videojuegos = {}
    clasificacion_videojuegos = {}
    
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

    def actualizar_videojuego(self, titulo, precio, stock):
        if titulo in self.inventario_videojuegos:
            self.stock_videojuegos[titulo] = stock
            self.precio_videojuegos[titulo] = precio
            print(f"Se ha actualizado el videojuego {titulo}, con un precio de {precio} y un stock de {stock}")
        else:
            print(f"El videojuego de titulo {titulo}, no se encuentra en el inventario")              
            
class Videojuego(Inventario):
    def __init__(self, titulo, plataforma, precio, stock, genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.stock = stock  
        self.genero = genero
        
        if self.titulo not in self.inventario_videojuegos:
            print(f"Se ha agregado el videojuego {self.titulo} al inventario")

            self.inventario_videojuegos.append(self.titulo)
            self.precio_videojuegos[self.titulo] = self.precio
            self.stock_videojuegos[self.titulo] = self.stock
         
            for genero in self.genero:
                if genero in self.genero_videojuegos:
                    self.genero_videojuegos[genero].append(self.titulo)
                else:
                    self.genero_videojuegos[genero] = [self.titulo]

        else:
            print(f"!El videojuego {self.titulo} ya se encuentra en el inventario")       

class VideojuegoPC(Videojuego):
    def __init__(self, titulo, plataforma, precio, stock, genero, requisitos_minimos):
        super().__init__(titulo, plataforma, precio, stock, genero)
        self.requisitos_minimos = requisitos_minimos
        self.requisitos_videojuegos[self.titulo] = self.requisitos_minimos

class VideojuegoConsola(Videojuego):
    def __init__(self, titulo, plataforma, precio, stock, genero, clasificacion):
        super().__init__(titulo, plataforma, precio, stock, genero)
        self.clasificacion = clasificacion 
        self.clasificacion_videojuegos[self.titulo] = self.clasificacion
        
class Cliente(Inventario):
    contador_carrito = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.productos_carrito = []

    def tomar_carrito(self):
        Cliente.contador_carrito += 1
        print(f"El Cliente {self.nombre} {self.apellido} a tomado el carrito {self.contador_carrito}")

    def agregar_productos(self, cantidad, *videojuegos_comprados):
        self.cantidad = cantidad

        for videojuego in videojuegos_comprados:
            if videojuego in self.inventario_videojuegos:
                self.productos_carrito.append(videojuego)
                print(f"-El videojuego {videojuego} se ha agregado al carrito")
            else:
                print(f"El videojuego {videojuego} no se encuentra en la tienda")
                return

        print("Todos los videojuegos se han agregado al carrito.")

    def realizar_compra(self):
        total_compra = 0
        
        for videojuego in self.productos_carrito:
            precio_videojuego = self.precio_videojuegos[videojuego] * self.cantidad
            total_compra = total_compra + precio_videojuego
            self.stock_videojuegos[videojuego] -= self.cantidad

        print(f"El total de la compra de {self.nombre} {self.apellido} es: ${total_compra}")