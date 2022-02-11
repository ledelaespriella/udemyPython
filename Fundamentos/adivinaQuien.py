from random import *

name= input('Cual es tu nombre: ')
print('Piensa en un numero entre 1 y el 100, recuerda que solo tienes 8 intentos para lograrlo.\n')
aleatorio= randint(1,100)
for e in range(1,9):
    num=int(input('Numero: '))
    if num == aleatorio:
        print(f'Felicidades {name} has acertado el numero en el intento {e}')
        break
    elif num<1 or num>100:
        print(f'Lo siento {name}, El numero elegida esta fuera del rango. Intente de nuevo')
    elif num<aleatorio:
         print(f'Lo siento {name}, El numero es menor al secreto. Intente de nuevo')
    elif num>aleatorio:
         print(f'Lo siento {name}, El numero es mayor al secreto. Intente de nuevo')
    
    if e==8 and num!=aleatorio:
        print(f'Lo siento {name},No has podido adivinar el numero secreto: {aleatorio}')
            
    
    
    

