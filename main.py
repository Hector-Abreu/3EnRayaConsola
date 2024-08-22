from tablero import Tablero

juego = Tablero()
contador = 0
jugador = "X"

while not juego.fin:
    contador = contador + 1
    print(f"Turno {contador}\n")
    if jugador == juego.jugadorActual:
      print("Jugador 1")
    else:
       print("Jugador 2")
    juego.print()
    fila = int(input("Selecciona fila (0,1,2): "))
    columna = int(input("Selecciona columna (0,1,2): "))
    juego.movimiento(fila, columna)
    print("\n")

juego.print()