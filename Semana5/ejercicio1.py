"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n,lista):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    for i in range(n):
        lista.append(i+1)

numeros = []
n = int(input("Ingrese hasta que numero llegue la lista:   "))
contar_ciclo(n,numeros)
print(numeros)

def contar_recursivo(n,lista):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    if n == 0:
        return
    else:
        lista.append(n)
        contar_recursivo(n-1,lista)

lista1 = []
n1 = int(input("Ingrese un numero:  "))
contar_recursivo(n1,lista1)
print(lista1)