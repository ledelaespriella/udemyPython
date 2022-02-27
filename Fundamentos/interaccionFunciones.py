from random import shuffle

#lista inicial
palitos=['-','--','---','----']

#mezclar palitos
def mezclar(lista):
    """Funcion que mezcla"""
    shuffle(lista)
    return lista

#pedirle intento
def probarSuerte():
    intento =''

    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')

    return int(intento)

#comprobar intento
def chequearIntento(lista,intento):
    if lista[intento-1]=='-':
        print('A lavar los platos')
    else:
        print('esta vez te has salvado')

    print(f'Te ha tocado {lista[intento -1]}')

palitosMezclados= mezclar(palitos)
seleccion= probarSuerte()

chequearIntento(palitosMezclados,seleccion)