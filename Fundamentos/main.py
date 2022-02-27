from random import *

#Trabajando con strings

mi_text = "Mi nombre es, luis"
result = mi_text[::-1]
#print(result)

#metodos de un strings
upper = mi_text.upper()
# print(f'texto en mayuscula {upper}')
lower = mi_text.lower()
# print(f'texto en minuscula {lower}')
split = mi_text.split(' ')
# print(f'texto separado en comas: {split}')
join = " ".join(split)
# print(f'texto con join {join}')
"""Practicando con ZIP"""

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado = zip(capitales, paises)

# for capital,pais in combinado:
# print(f'La capital de {capital} es {pais}')
"""Practicando con random"""
colores = ['azul', 'rojo', 'amarillo']

aleatorio = random()
aleatorioColor=choice(colores)

# print(aleatorioColor)
"""Compresion de listas"""

palabra='python'

lista= [letra for letra in palabra]

"""PRACTICANDO MATCH en version 3.10"""

serio = "N-02"

match serio:
    case "N-01":
        print('samsung')
    case "N-02":
        print('nokia')

def suma(*args,**kwargs):
    return sum(args)

print(suma(1))