#AI-TRAP:ESTRUCTURAL
# Este ejercicio invierte una lista, útil en procesamiento de datos históricos o manipulación de secuencias.

def invertir_lista(lista):
    for i in range(len(lista)//2):
        temp = lista[i]
        lista[i] = lista[len(lista)-i-1]
        lista[len(lista)-i-1] = temp
    return lista

print(invertir_lista([1,2,3,4,5,6,7,8,9,10,11]))

#Suma y numero maximo 

def suma_y_maximo(lista):
    if not lista:
        return 0, None
    
    suma = 0
    maximo = lista[0]
    
    for numero in lista:
        suma += numero
        if numero > maximo:
            maximo = numero
            
    return suma, maximo

numeros = [1,2,3,4,5,6,7,8,9,10,11]
suma_total, numero_maximo = suma_y_maximo(numeros)
print(f"La suma es: {suma_total}")
print(f"El número más alto es: {numero_maximo}")

























