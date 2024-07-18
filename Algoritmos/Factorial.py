def factorial(n): 
    result = 1 
    for i in range(1, n + 1): 
        result = result * i 
    return result

numero = int (input("Ingrese un numero entero no negativo: "))

resultado = factorial(numero)
print("El factorial de: ", numero, " es ", resultado)