"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""

def FfiBo(num):
    n0=0
    n1=1
    fibo=[0]
    for i in range(num):
        fb=n0+n1
        n0=n1
        n1=fb
        fibo.append(fb)
        if len(fibo)==50:
            print(fibo)
            break

  

FfiBo(522)