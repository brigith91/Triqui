Tablero: list[list[str]] = [
    ['*', '*', '*', ],
    ['*', '*', '*', ],
    ['*', '*', '*', ],

]


def imprimir_tablero(tab):

    print('     0   1   2')
    for num_fila, fila, in enumerate(tab): 
        print(num_fila, end=' ↾ ')  # recorre tablero
        for casilla in fila:  # recorre columnas
            print(casilla, end=' ↿ ')
        print(num_fila)
        if num_fila < 2:  # imprime la fila
            print(' ----------------')
    print('     0   1   2')


imprimir_tablero(Tablero)
