"""
Ejercicio 7:
Una persona registra cuánto dinero ahorra cada mes en una lista.
Cada valor representa el ahorro mensual.

Se requiere calcular el ahorro total acumulado.

Debe implementar:
1. Una solución con iteración
2. Una solución con recursividad
"""

def ahorro_total_ciclo(ahorros):
    """
    Retorna el ahorro total usando iteración.
    """
    resultado = 0
    for ahorros in ahorros:
        resultado = resultado + ahorros
    return resultado

ahorros1 = [120000, 130000,125000,100000]
print(ahorro_total_ciclo(ahorros1))

def ahorro_total_recursivo(ahorros):
    """
    Retorna el ahorro total usando recursividad.
    """
    if ahorros:

