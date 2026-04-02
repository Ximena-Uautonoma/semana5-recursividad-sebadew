"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado = 1
    for i in range(1,exponente+1):
        resultado = resultado * base
    return resultado

base1 = int(input("Ingrese la base:   "))
exponente1 = int(input("Ingrese el exponente:   "))
print(potencia_ciclo(base1,exponente1))

def potencia_recursiva(base, exponente):
    if exponente==1:
        return base
    else:
        return potencia_recursiva(exponente-1,base)*base

base2 = int(input("Ingrese la base:   "))
exponente2 = int(input("Ingrese el exponente:   "))
print(potencia_ciclo(base2,exponente2))