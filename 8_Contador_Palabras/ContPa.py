""""/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */"""
from unidecode import unidecode
 
# Abre el archivo "palabras.txt" en modo de lectura y codificación 'utf-8'
with open("palabras.txt", "r", encoding='utf-8') as archivo:
        parrafos = archivo.read().split("\n")

len_parrafos = len(parrafos)

 # Define el método 'separar_palabras'
class contador_palabras():
    def __init__(self, parrafos):
        self.parrafos = parrafos
        self.Lista = []
        
    def separar_palabras(self):
        for palabras in parrafos:
             # Elimina los caracteres especiales al principio y al final de 'palabras', convierte 'palabras' a minúsculas, lo divide en palabras por cada espacio
            self.palabras = palabras.strip("'.,;:?¿!¡/© ()").lower().split(" ")
            self.Lista.append(self.palabras)
        palabras_separadas = []
        for lista_palabras in self.Lista:
            for palabra in lista_palabras:
                palabras_separadas.append(palabra)
        
        palabras_separadas = [unidecode(palabra) for palabra in palabras_separadas if palabra != ""]
        
        counter: dict = {}
        
        for palabra in palabras_separadas:
            if palabra in counter:
                counter[palabra] += 1
            else:
                counter[palabra] = 1
        print(counter)
        
        return counter
  
lista = contador_palabras(parrafos)
lista0 = lista.separar_palabras()
print(lista0)