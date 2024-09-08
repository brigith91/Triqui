Tablero: list[list[str]] = [
    ['*', '*', '*', ],
    ['*', '*', '*', ],
    ['*', '*', '*', ],

]


def imprimir_tablero(tab):
    print('    0, 1, 2')
    for i, fila in enumerate(tab): 
        print(i, end=' | ')  # recorre tablero
        for casilla in fila:  # recorre columnas
            print(casilla, end='  ')  # imprime la fila
        print('\n-----------')
    print('    0, 1, 2')


imprimir_tablero(Tablero)
