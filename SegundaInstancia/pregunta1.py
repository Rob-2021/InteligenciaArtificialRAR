import sys
from collections import deque 

#Búsqueda primero en amplitud
# Las siguientes listas detallan los cuatro movimientos posibles desde una celda
# arriba: (x, y) -> (x - 1, y)
# izquierda: (x, y) -> (x, y - 1)
# abajo: (x, y) -> (x + 1, y)
# derecha: (x, y) -> (x, y + 1)

# fila = [-1, 0, 0, 1]
# col = [0, -1, 1, 0]

#diagonal
fila = [-1, -1, -1, 0, 1, 0, 1, 1] 
col = [-1, 1, 0, -1, -1, 1, 0, 1]

# Función para comprobar si es posible ir a la posición (fila, columna)
# desde la posición actual. La función devuelve falso si fila, columna
# no es una posición válida o tiene valor 0 o ya fue visitada.
def esValido(mat, visitado, fila, col):
    return (fila >= 0) and (fila < len(mat)) and (col >= 0) and (col < len(mat[0])) \
           and mat[fila][col] == 1 and not visitado[fila][col]
 
 
# Encuentra la ruta más corta posible en una matriz `mat` desde el origen `src` hasta
# destino `dest`
def longitudRutaCorta(mat, src, dest):
 
    # obtener celda origen (i, j)
    i, j = src
 
    # obtener celda de destino (x, y)
    x, y = dest
 
    # Caso base: entrada no válida
    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return -1
 
    # Matriz `M × N`
    (M, N) = (len(mat), len(mat[0]))
 
    # construye una matriz para realizar un seguimiento de las celdas visitadas
    visitado = [[False for x in range(N)] for y in range(M)]
 
    # crea una cola vacía
    q = deque()
 
    # marcar la celda de origen como visitada y poner en cola el nodo de origen
    visitado[i][j] = True
 
    # (i, j, dist) representa las coordenadas de las celdas de la matriz y sus
    # distancia mínima de la origen
    q.append((i, j, 0))
 
    # almacena la longitud de la ruta más larga desde el origen hasta el destino
    min_dist = sys.maxsize
 
    # Bucle # hasta que la cola esté vacía
    while q:
 
        # quitar la cola del nodo frontal y procesarlo
        (i, j, dist) = q.popleft()
 
        # (i, j) representa una celda actual, y `dist` almacena su
        # distancia mínima de la origen
 
        # si se encuentra el destino, actualice `min_dist` y pare
        if i == x and j == y:
            min_dist = dist
            break
 
        # verifica los cuatro movimientos posibles desde la celda actual
        # y poner en cola cada movimiento válido
        # for k in range(4):
        #     # comprobar si es posible ir a la posición
        #     # (i + fila[k], j + col[k]) desde la posición actual
        #     if esValido(mat, visitado, i + fila[k], j + col[k]):
        #         # marca la siguiente celda como visitada y la pone en cola
        #         visitado[i + fila[k]][j + col[k]] = True
        #         q.append((i + fila[k], j + col[k], dist + 1))


        for k in range(8):
            # comprobar si es posible ir a la posición
            # (i + fila[k], j + col[k]) desde la posición actual
            if esValido(mat, visitado, i + fila[k], j + col[k]):
                # marca la siguiente celda como visitada y la pone en cola
                visitado[i + fila[k]][j + col[k]] = True
                q.append((i + fila[k], j + col[k], dist + 1))
 
    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1
 
 
if __name__ == '__main__':
 
    mat = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]
 
    src = (0, 0)
    dest = (9, 9)
 
    min_dist = longitudRutaCorta(mat, src, dest)
 
    if min_dist != -1:
        print("El camino más corto desde el origen hasta el destino tiene una longitud", min_dist)
    else:
        print("No se puede llegar al destino desde el origen")
