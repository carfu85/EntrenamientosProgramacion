"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""
 
 
def anagrama(palabra1, palabra2):
    if palabra1 == palabra2:
        return False
    else:
        palabra1 = sorted(palabra1)
        palabra2 = sorted(palabra2)

        if palabra1 == palabra2:
            return f'El resultado de anagrama: {True}'
        else:
            return f'El resultado de anagrama: {False}'


def anagrama2 (palabra1, Palabra2):
    letrasPal1=[]
    letrasPal2=[]
    if len(palabra1) != len(Palabra2):
        return False
    else:
        for letra in palabra1:
            letrasPal1.append(letra)
        
        for letra in Palabra2:
            letrasPal2.append(letra)
        existe=False
        
        for letra in letrasPal1:
            if letra not in letrasPal2:
                existe=False
                break
            else:
                existe=True
                
        if existe==True:
            return True
        else:
            return False 

print(anagrama("amor", "roma"))
print(anagrama("amor", "romas"))
print(anagrama("amor", "romass"))
print(anagrama('Rosa', 'Arbol'))


print(anagrama2("amor", "roma"))
print(anagrama2("amor", "romas"))
print(anagrama2("amor", "romass"))
print(anagrama2('Rosa', 'Arbol'))