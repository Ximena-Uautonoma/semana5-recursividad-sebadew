"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def total_ventas_ciclo(ventas):
    """
    Retorna el total de ventas usando ciclos.
    """
    # Escriba aquí su solución
    resultado = 0
    for ventas in ventas:
        resultado = resultado + ventas
    return resultado

venta1 = [100000,100000]
print(total_ventas_ciclo(venta1))


def total_ventas_recursivo(ventas):
    """
    Retorna el total de ventas usando recursividad.
    """
    # Escriba aquí su solución
    if len(ventas) == 0:
        return 0
    else:
        return ventas[0] + total_ventas_recursivo(ventas[(0+1):])

venta2 = [100000,100000,150000]
print(total_ventas_recursivo(venta2))