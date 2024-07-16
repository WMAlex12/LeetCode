def buscar_subcadena(cadena, subcadena):
    n = len(cadena)
    m = len(subcadena)
    ## Lista vacia que funciona para almacenar las posiciones de las ocurrencias encontradas
    ocurrencias = []
    
    for i in range(n - m + 1): 
        j = 0
        ##Comparacion de los caracteres de la subcadena con la cadena principal 
        while j<m : 
            if cadena[i + j] != subcadena[j]: 
                break
            j += 1 
        if j == m: 
            ocurrencias.append(i)
    return ocurrencias

cadena_principal  = "abracadabra" 
subcadena_busqueda = "ra"
resultados = buscar_subcadena(cadena_principal, subcadena_busqueda)
print("Ocurrencias encontradas en la posicion: ", resultados)    
