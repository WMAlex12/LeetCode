
def busqueda_secuencial(lista,elemento): 
    for i in range(len(lista)): 
        if(lista[i] == elemento): 
            return i+1 
    return -1

mi_lista = [1,3,6,9,2]
elemento_buscado = 6

resultado = busqueda_secuencial(mi_lista, elemento_buscado)
if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en la posicion {resultado}") 
else: 
    print(f"El elemento {elemento_buscado} no se encuentra en la lista")