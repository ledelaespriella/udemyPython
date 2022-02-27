import os
from pathlib import Path



# ruta=os.getcwd()
# print('')
# print(ruta)
'''Aprendiendo de PATHLIB'''
carpeta=Path('/Users/luisdelaespriella/Desktop/PERSONAL/CURSOS/PROGRAMACION/MINTIC 2022/CICLO 1/PRACTICAS PYTHON') /'archivo.txt'
base=Path.home()
# print(carpeta.parents[2])
print(carpeta.stem)

"""Limpieza de consola"""

n=input('Nombre: ')
edad=input('Edad: ')
os.system('clear')

print(f'Hola {n} tienes {edad}')
