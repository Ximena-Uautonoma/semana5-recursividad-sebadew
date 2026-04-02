"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    resultado = 0
    for i in range(1,n+1):
        if (i%2) == 0:
            resultado = resultado + 1
    return resultado


def contar_pares_recursivo(n):
    resultado = 0
    if (n==1):
        return 0
    else:
        if (n%2) == 0:
            resultado = resultado + 1
            contar_pares_recursivo(n-1)
        else:
            contar_pares_recursivo(n-1)
        

