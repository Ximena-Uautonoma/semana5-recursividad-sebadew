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

numero1 = int(input("Ingrese un numero:   "))
printc(contar_pares_ciclo(numero1))

def contar_pares_recursivo(n):
    if n==0:
        return 0
    elif (n%2) == 0:
        return contar_pares_recursivo(n-1)+1
    else:
        return contar_pares_recursivo(n-1)
        
numero2 = int(input("Ingrese un numero:   "))
printc(contar_pares_recursivo(numero2))
