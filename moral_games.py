class Videojuego:
    def __init__(self, titulo, plataforma, precio, stock, genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.stock = stock  
        self.genero = genero    

class VideojuegoPc(Videojuego):
    def __init__(self, titulo, plataforma, precio, stock, genero, requisitos_minimos):
        super().__init__(titulo, plataforma, precio, stock, genero)
        self.requisitos_minimos = requisitos_minimos   

        
class VideojuegoConsola(Videojuego):
    def __init__(self, titulo, plataforma, precio, stock, genero, clasificacion):
        super().__init__(titulo, plataforma, precio, stock, genero)
        self.clasificacion = clasificacion


class Inventario:
    genero_videojuegos = {}
    inventario_videojuegos = [] 
    precio_videojuegos = {}
    stock_videojuegos = {}
    requisitos_videojuegos = {}
    clasificacion_videojuegos = {}
    
    def agregar_videojuego(self, videojuego):
        try:
            if videojuego.precio <= 0 or videojuego.stock <= 0:
                print(f"El stock y precio del videojuego {videojuego.titulo}, debe ser mayor a 0")
                return
        except TypeError:
            print(f"El precio y el stock del videojuego {videojuego.titulo} deben ser numeros naturales")
            return

        if videojuego.titulo not in self.inventario_videojuegos:
            print(f"Se ha agregado el videojuego {videojuego.titulo} al inventario.")

            self.inventario_videojuegos.append(videojuego.titulo)
            self.precio_videojuegos[videojuego.titulo] = videojuego.precio
            self.stock_videojuegos[videojuego.titulo] = videojuego.stock

            if isinstance(videojuego, VideojuegoPc):
                self.requisitos_videojuegos[videojuego.titulo] = videojuego.requisitos_minimos
            elif isinstance(videojuego, VideojuegoConsola):
                self.clasificacion_videojuegos[videojuego.titulo] = videojuego.clasificacion
            
            if videojuego.genero in self.genero_videojuegos:
                self.genero_videojuegos[videojuego.genero].append(videojuego.titulo)
            else:
                self.genero_videojuegos[videojuego.genero] = [videojuego.titulo]

        else:
            print(f"!El videojuego {videojuego.titulo} ya se encuentra en el inventario")       

    def actualizar_videojuego(self, titulo, precio, stock):
        if precio <= 0 or stock <= 0:
            print(f"El stock y precio del videojuego {titulo}, debe ser mayor a 0")
            return
        
        if titulo in self.inventario_videojuegos:
            self.stock_videojuegos[titulo] = stock
            self.precio_videojuegos[titulo] = precio
            print(f"Se ha actualizado el videojuego {titulo}, con un precio de {precio} y un stock de {stock}")
        else:
            print(f"El videojuego de titulo {titulo}, no se encuentra en el inventario")    
        
class Cliente:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def buscar_videojuego(self, videojuego_genero):
        print(f"Se busco '{videojuego_genero}', se encontro: ")

        if videojuego_genero in Inventario.genero_videojuegos:
            lista_generos = Inventario.genero_videojuegos[videojuego_genero]

            for videojuego in lista_generos:
                print(f"-{videojuego}")
            print("\n")

        elif videojuego_genero in Inventario.inventario_videojuegos:
            print(f"-{videojuego_genero}")
        else:
            print(f"El videojuego o genero, no se encuentra en el inventario")

    def mostrar_videojuegos(self):
        if Inventario.inventario_videojuegos:
            print("\nLos videojuegos que se encuentran en la tienda son:")

            for juego in Inventario.inventario_videojuegos:
                print(f"-{juego}")
            print("\n")

        else:
            print("No hay videojuegos en el inventario de la tienda")

    def mostrar_requisitos(self, titulo):
        if titulo in Inventario.requisitos_videojuegos:
            print(f"Los requisitos minimos del videojuego {titulo} son {Inventario.requisitos_videojuegos[titulo]}\n")
        else:
            print("El videojuego debe ser de pc\n")

    def mostrar_clasificacion(self, titulo):
        if titulo in Inventario.clasificacion_videojuegos:
            print(f"La clasificacion del videojuego {titulo} es {Inventario.clasificacion_videojuegos[titulo]}\n")
        else:
            print("\nEl videojuego debe ser de consola")        
    
class Carrito:
    contador_carrito = 0    

    def __init__(self, cliente):
        Carrito.contador_carrito += 1
        self.productos_carrito = []

        print(f"El cliente {cliente.nombre} {cliente.apellido} a tomado el carrito {self.contador_carrito}")

    def agregar_productos(self, cantidad, *videojuegos_comprados):
        self.cantidad = cantidad

        for videojuego in videojuegos_comprados:
            if videojuego in Inventario.inventario_videojuegos:
                stock_disponible = Inventario.stock_videojuegos[videojuego]

                if self.cantidad > stock_disponible:
                    print(f"No se pueden agregar {self.cantidad} unidades del videojuego {videojuego}, Se agregarán las {stock_disponible} unidades disponibles al carrito")
                    self.cantidad = stock_disponible
                    
                self.productos_carrito.append(videojuego)
                Inventario.stock_videojuegos[videojuego] -= self.cantidad
                print(f"-El videojuego {videojuego} se ha gregado al carrito de {self.nombre} con una cantidad de {self.cantidad} unidades")

            else:
                print(f"El videojuego {videojuego} no se encuentra en la tienda")
                return
            
        print("Todos los videojuegos se han agregado al carrito \n")

    def realizar_compra(self):
        total_compra = 0

        if not self.productos_carrito:
            print(f"El cliente {self.nombre} {self.apellido}, No ha agregado productos al carrito aun")
            return
        
        for videojuego in self.productos_carrito:
            precio_videojuego = self.precio_videojuegos[videojuego] * self.cantidad
            total_compra = total_compra + precio_videojuego

        print(f"El total de la compra de {self.nombre} {self.apellido} es: ${total_compra}")