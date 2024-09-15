import os


Tablero = (
    ['*', '*', '*', ],  # 0
    ['*', '*', '*', ],  # 1
    ['*', '*', '*', ],  # 2
)

def limpiar_pantalla() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_tablero(tab: tuple[list[str], ...]) -> None:

    print('    A    B    C')

    nombres_filas = 'XYZ'

    for numero_fila, fila, in enumerate(tab):
        nom_fila = nombres_filas[numero_fila].lower()

        print(nom_fila, end=' ↾ ')

        for col in fila:  # recorre columnas
            print(col, end=' ↿ ')

        print(nom_fila)
        if numero_fila < 2:  # imprime la fila
            print(' ----------------')

    print('    A    B    C')

def leer_posicion() -> tuple[int, int]:
    posicion: str = input('Ingrese una posicion (ej: xC): ')

    fila_str: str = posicion[0].lower()
    columna_str: str = posicion[1].upper()

    nombres_columnas: str = 'ABC'
    nombres_filas: str = 'xyz'

    fila_idx: int = nombres_filas.find(fila_str)  # idx=indice
    columna_idx: int = nombres_columnas.find(columna_str)  

    return fila_idx, columna_idx


def realizar_jugada(
    ficha: str,
    tab: tuple[list[str], ...],
    pos: tuple[int, int]
) -> bool:
    
    movimiento_valido: bool = False

    if pos[0] >= 0 and pos[1] >= 0:
    
        if tab[pos[0]][pos[1]] == '*':
            tab[pos[0]][pos[1]] = ficha
            movimiento_valido = True

    return movimiento_valido


def validar_empate(tab: tuple[list[str], ...]) -> bool:
    hay_empate: bool = True

    for fila in tab:
        for col in fila:
            if col == '*':
                hay_empate = False

    return hay_empate


def verificar_ganador(tab: tuple[list[str], ...]) -> str | None:
    ganador: str | None = None



    for num_fila in range(3):
        if tab[num_fila][0] == tab[num_fila][1] == tab[num_fila][2] and tab[num_fila][0] != '*':
            ganador = tab[num_fila][0]

    for num_columna in range(3):
        if tab[0][num_columna] == tab[1][num_columna] == tab[2][num_columna] and tab[0][num_columna] != '*':
            ganador = tab[0][num_columna]

    if tab[0][0] == tab[1][1] == tab[2][2] and tab[1][1] != '*':
        ganador = tab[0][0]

    if tab[2][0] == tab[1][1] == tab[0][2] and tab[1][1] != '*':
        ganador = tab[2][0]

    return ganador

def jugar() -> None:
    turno: str = 'X'
    ganador: str | None = None

    while ganador is None:
        
        limpiar_pantalla()
        ganador = verificar_ganador(Tablero)
        if ganador is None:
            if validar_empate(Tablero):
                ganador = 'Empate'
            else:
                if turno == 'X':
                    turno = 'O'
                else:
                    turno = 'X'
        
        imprimir_tablero(Tablero)
        print(f'Es el turno de {turno}')
        fila, col = leer_posicion()
        jugada_valida: bool =realizar_jugada(turno,Tablero, (fila, col))

        if not jugada_valida:
            print('Jugada invalida, vuelve a jugar')

    if ganador == 'Empate':
        print('Juego empatado buen juego')
    else:
        print(f'El ganador del juego es {ganador}, Buen juego!')

jugar()




