from moral_games import Videojuego, VideojuegoPc, VideojuegoConsola, Inventario, Cliente, Carrito, Compra

#Crear videojuegos
juego1 = VideojuegoConsola("Resident Evil 4", "Consola", 38, 100, "Survival Horror", "D")
juego2 = VideojuegoConsola("Fifa 21", "Consola", 70, 100, "Deportes", "A")

juego3 = Videojuego("Need For Speed Most Wanted", "Consola", 40, 100, "Carreras")

juego4 = VideojuegoPc("Grand Theft Auto San Andreas", "PC", 100, 100, "Mundo Abierto", "1Ghz, 256MB RAM. 64MB Geforce, 3.6GB")
juego5 = VideojuegoPc("Call of Duty Blacks Ops 2", "PC", 60, 100, "Accion", "2.66GHz, 2GB RAM, 512MB Nvidia, 16GB")

#Agregar videojuegos al inventario
inventario = Inventario()
inventario.agregar_videojuego(juego1)
inventario.agregar_videojuego(juego2)
inventario.agregar_videojuego(juego3)
inventario.agregar_videojuego(juego4)
inventario.agregar_videojuego(juego5)

#actualizacion videojuego
inventario.actualizar_videojuego("Need For Speed Most Wanted", 21, 21)

#Acciones del cliente
cliente1 = Cliente("Tom", "Holland")
cliente1.mostrar_videojuegos()
cliente1.buscar_videojuego("Deportes")
cliente1.mostrar_clasificacion("Resident Evil 4")
cliente1.mostrar_requisitos("Call of Duty Blacks Ops 2")

#Toma de carrito
cliente1 = Carrito(cliente1)
cliente1.agregar_productos(10, "Resident Evil 4", "Call of Duty Blacks Ops 2")
cliente1.mostrar_productos()

#Compra del cliente
cliente1 = Compra(cliente1)
cliente1.realizar_compra()