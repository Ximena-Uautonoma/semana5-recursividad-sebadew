"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    """
    Retorna la suma de los primeros n números usando un ciclo.
    """
    resultado = 0
    for i in range(n+1):
        resultado = resultado + i
    return resultado

numero1 = int(input("Ingrese hasta que numero se suma: "))
print(suma_ciclo(numero1))



def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
    """
    if n == 1:
        return 1
    else:
        return suma_recursiva(n-1)+n

numero2 = int(input("Ingrese hasta que numero se suma: "))
print(suma_recursiva(numero2))