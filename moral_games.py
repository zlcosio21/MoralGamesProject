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
        if precio <= 0 or stock <= 0:
            print(f"El stock y precio del videojuego {self.titulo}, debe ser mayor a 0")
            return
        
        if titulo in self.inventario_videojuegos:
            self.stock_videojuegos[titulo] = stock
            self.precio_videojuegos[titulo] = precio
            print(f"Se ha actualizado el videojuego {titulo}, con un precio de {precio} y un stock de {stock}")
        else:
            print(f"El videojuego de titulo {titulo}, no se encuentra en el inventario")    

    def mostrar_requisitos(self, titulo):
        if titulo in self.requisitos_videojuegos:
            print(f"Los requisitos minimos del videojuego {titulo} es {self.requisitos_videojuegos[titulo]}")
        else:
            print("El videojuego debe ser de pc")

    def mostrar_clasificacion(self, titulo):
        if titulo in self.clasificacion_videojuegos:
            print(f"La clasificacion del videojuego {titulo} es {self.clasificacion_videojuegos[titulo]}")
        else:
            print("El videojuego debe ser de consola")
            
class Videojuego(Inventario):
    def __init__(self, titulo, plataforma, precio, stock, genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.stock = stock  
        self.genero = genero

        try:
            if self.precio <= 0 or self.stock <= 0:
                print(f"El stock y precio del videojuego {self.titulo}, debe ser mayor a 0")
                return
        except TypeError:
            print(f"El precio y el stock del videojuego {self.titulo} deben ser numeros naturales")
            return
        
        
        if self.titulo not in self.inventario_videojuegos:
            print(f"Se ha agregado el videojuego {self.titulo} al inventario")

            self.inventario_videojuegos.append(self.titulo)
            self.precio_videojuegos[self.titulo] = self.precio
            self.stock_videojuegos[self.titulo] = self.stock
            
            if self.genero in self.genero_videojuegos:
                self.genero_videojuegos[self.genero].append(self.titulo)
            else:
                self.genero_videojuegos[self.genero] = [self.titulo]

        else:
            print(f"!El videojuego {self.titulo} ya se encuentra en el inventario")       

class VideojuegoPc(Videojuego):
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
        self.carrito_tomado = False

    def tomar_carrito(self):
        Cliente.contador_carrito += 1
        self.carrito_tomado = True
        print(f"El cliente {self.nombre} {self.apellido} a tomado el carrito {self.contador_carrito}")

    def agregar_productos(self, cantidad, *videojuegos_comprados):
        self.cantidad = cantidad

        if not self.carrito_tomado:
            print(f"El cliente {self.nombre} {self.apellido} no ha tomado un carrito aun")
            return
        
        for videojuego in videojuegos_comprados:
            if videojuego in self.inventario_videojuegos:
                stock_disponible = self.stock_videojuegos[videojuego]

                if self.cantidad > stock_disponible:
                    self.cantidad = stock_disponible
                    print(f"No se pueden agregar {self.cantidad} unidades del videojuego {videojuego}, Se agregarán las {stock_disponible} unidades disponibles al carrito")

                self.productos_carrito.append(videojuego)
                self.stock_videojuegos[videojuego] -= self.cantidad
                print(f"-El videojuego {videojuego} se ha agregado al carrito")
                print("Todos los videojuegos se han agregado al carrito.")

            else:
                print(f"El videojuego {videojuego} no se encuentra en la tienda")
                return

    def realizar_compra(self):
        total_compra = 0

        if not self.productos_carrito:
            print(f"El cliente {self.nombre}, {self.apellido}, No ha agregado productos al carrito aun")
            return
        
        for videojuego in self.productos_carrito:
            precio_videojuego = self.precio_videojuegos[videojuego] * self.cantidad
            total_compra = total_compra + precio_videojuego

        print(f"El total de la compra de {self.nombre} {self.apellido} es: ${total_compra}")