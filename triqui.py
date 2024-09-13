Tablero: list[list[str]] = [
    ['*', '*', '*', ], #0
    ['*', '*', '*', ], #1
    ['*', '*', '*', ], #2

]


def imprimir_tablero(tab: list[list[str]])-> None:

    print('    A  B   C')
    nombres_filas = 'XYZ'

    for num_fila, fila, in enumerate(tab):
        nom_fila = nombres_filas[num_fila]

        print(nom_fila, end=' ↾ ') 

        for casilla in fila:  # recorre columnas
            print(casilla, end=' ↿ ')

        print(nom_fila)
        if num_fila < 2:  # imprime la fila
            print(' ----------------')

    print('    A  B   C')

def leer_posicion()-> tuple[int,int]:
    posicion: str =input("Ingrese una pocision (ej: xC:) ")

    fila_str: str = posicion[0]
    columna_str: str =posicion[1]

    return fila_str, columna_str



imprimir_tablero(Tablero)

fila, columna =leer_posicion

print(f"la posicion leida es : {fila}")
