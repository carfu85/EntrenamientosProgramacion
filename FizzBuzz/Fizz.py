"""Fiz Buzz Program 
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
 """
 

class FizzBuzz:
    def __init__(self):
        self.fizz = 3
        self.buzz = 5
        for i in range(1,101):
            self.impresion=self.fizzbuzz(i)
        
    def fizzbuzz(self, numero):
        self.numero = numero
        if self.numero % self.fizz == 0 and self.numero % self.buzz == 0:
            print(f'\nFizzBuzz')
        elif self.numero % self.fizz == 0:
            print(f'\nFizz')
        elif self.numero % self.buzz == 0:
            print(f'\nBuzz')
        else:
            print(f'\n{self.numero}')
            
if __name__ == '__main__':
    fizzbuzz = FizzBuzz()
  
          