from colorama import init, Fore, Style

class Tablero:
  # Constructor  
  def __init__(self):
    self.tablero = [[" " for _ in range(3)] for _ in range(3)]
    self.jugadorActual = "X"
    self.fin = False

  def print(self):
    init(autoreset=True)
    for i in range(2, -1, -1):  # Recorre las filas del tablero en orden inverso
      for j in range(3):
        celda = self.tablero[i][j]
        color = Fore.RED if celda == "X" else Fore.YELLOW
        print(f"{color}{celda}", end=" | ")
      print("\n" + "-" * 13)
    print(Style.RESET_ALL) 

  def movimiento(self, fila, columna):
    color = Fore.GREEN
    color2 = Fore.YELLOW
    if not self.fin and self.tablero[fila][columna] == " ":
      self.tablero[fila][columna] = self.jugadorActual
      if self.ganador(fila, columna):
        if self.jugadorActual == "X":
          print(f"\n{color}Jugador 1 ha ganado")
        else:
          print(f"\n{color}Jugador 2 ha ganado")
        self.fin = True
      elif self.tableroLleno():
        print(f"\n{color2}Empate")
        self.fin = True
      else:
        self.cambioTurno()

  def cambioTurno(self):
    self.jugadorActual = "X" if self.jugadorActual == "O" else "O"

  def tableroLleno(self):
    for fila in self.tablero:
      if " " in fila:
        return False
    return True

  def ganador(self, fila, columna):
    simbolo = self.tablero[fila][columna]
    return (self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] == simbolo or
      self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == simbolo or
      self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == simbolo or
      self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == simbolo)