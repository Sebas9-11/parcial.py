import math

# Calcula la distancia entre dos puntos
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Funciones para ordenar por x e y
def pointX(punto):
    return punto[0]

def pointY(punto):
    return punto[1]

def pares_cercanos(puntos, *args, **kwargs):
    # Ordena los puntos según las coordenadas x e y
    pointsX = sorted(puntos, key=pointX)
    pointsY = sorted(puntos, key=pointY)
    
    # Caso base: cuando hay menos de 3 puntos
    if len(pointsX) < 3:
        min_dist = float('inf')
        p1 = None
        p2 = None
        for i in range(len(pointsX)):
            for j in range(i+1, len(pointsX)):
                if distancia(pointsX[i], pointsX[j]) < min_dist:
                    min_dist = distancia(pointsX[i], pointsX[j])
                    p1, p2 = pointsX[i], pointsX[j]
        return p1, p2, min_dist

    # Divide los puntos
    middle = len(pointsX) // 2
    midpoint = pointsX[middle]
    
    # Divide y vencerás
    p1_left, p2_left, min_dist_left = pares_cercanos(pointsX[:middle], *args, **kwargs)
    p1_right, p2_right, min_dist_right = pares_cercanos(pointsX[middle:], *args, **kwargs)

    # Toma el par más cercano
    if min_dist_left < min_dist_right:
        d = min_dist_left
        min_pair = (p1_left, p2_left)
    else:
        d = min_dist_right
        min_pair = (p1_right, p2_right)

    # Comprueba puntos en la "franja" cerca de la línea divisoria
    strip = [p for p in pointsY if abs(p[0] - midpoint[0]) < d]
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) < d and distancia(strip[i], strip[j]) < d:
                d = distancia(strip[i], strip[j])
                min_pair = (strip[i], strip[j])
    return min_pair[0], min_pair[1], d

# Ejemplo de uso
puntos = [(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
print(pares_cercanos(puntos))
