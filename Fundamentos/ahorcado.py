from random import choice
#variables
palabras=['azucar','cafe','amor','descontrol']
letrasCorrectas=[]
letrasIncorrectas=[]
intento=6
aciertos=0
juegoTerminado=False

#elegir una palabra al azar
def palabraAzar(lista):
    palabraElegida=choice(lista)
    letrasUnicas= len(set(palabraElegida))
    return palabraElegida,letrasUnicas

def verificar(letra):
    '''Funcion que verifica que la letra sea un string'''
    if letra.isalpha:
        return True
    else:
        return False

#funcion para que pida una letra
def pedirLetra():
    letraElegida=''
    ver=False
    while not ver:
        letraElegida=input('Ingrese una letra: ')
        if verificar(letraElegida) and len(letraElegida)==1:
            ver=True
        else:
            print('No has elegido una letra valida')

    return letraElegida


def mostrarTablero(palabraElegida):
    '''Funcion para que muestre los guiones'''
    listaOculta=[]
    
    for l in palabraElegida:
        if l in letrasCorrectas:
            listaOculta.append(l)
        else:
            listaOculta.append('_')
    
    print(' '.join(listaOculta))
    
def chequearLetra(letra_elegida,palabraOculta,vidas,coincidencia):
    fin=False
    if letra_elegida in palabraOculta:
        letrasCorrectas.append(letra_elegida)
        coincidencia+=1
    else:
        vidas-=1
        letrasIncorrectas.append(letra_elegida)
        

    if vidas==0:
        fin=perder()
    elif coincidencia==letrasUnicas:
        fin=ganar(palabraOculta)

    return vidas,fin, coincidencia
        

def perder():
    print('Te has quedado sin vidas')
    print('La palabra oculta era: '+palabra)
    return True

def ganar(palabraDescubierta):
    mostrarTablero(palabraDescubierta)
    print('Felicidades has encontrado la palabra')
    return True


palabra,letrasUnicas=palabraAzar(palabras)
while not juegoTerminado:
    print('\n'+'*'*20+'\n')
    mostrarTablero(palabra)
    print('\n')
    print('Letras incorrectas: '+'-'.join(letrasIncorrectas))
    print(f'vidas: {intento}')
    print('\n'+'*'*20+'\n')
    letra=pedirLetra()

    intento, terminado, aciertos=chequearLetra(letra,palabra,intento,aciertos)
    
    juegoTerminado=terminado