"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    resultado = 1
    for i in range(1,n+1):
        resultado = resultado * i
    return resultado

numero1 = int(input("Ingrese numero: "))
print(factorial_ciclo(numero1))

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return factorial_recursivo(n-1)*n

numero2 = int(input("Ingrese numero: "))
print(factorial_recursivo(numero2))