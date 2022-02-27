import os
from pathlib import Path
from os import system as sys

mi_ruta=Path(Path.home(),'Desktop/PERSONAL/CURSOS/PROGRAMACION','UDEMY','PYTHON','FUNDAMENTOS',"archivos","recetas")

def contarRecetas():
    contador=0
    for txt in Path(mi_ruta).glob('**/*.txt'):
        contador+=1

    return contador

def inicio():
    sys('clear')
    print('*'*50)
    print('*'*5+' Bienvenido al administrador de recetas '+'*'*5)
    print('*'*50)
    print('\n')

    print(f'Las recetas se encuentran en {mi_ruta}')
    print(f'Total recetas: {contarRecetas()}')

    eleccion='x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1,7):
        print('Elige una opcion: ')
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar Categoria
        [6] - Salir del programa''')
        eleccion=input()
    
    return int(eleccion)

def mostrarCategoria(ruta):
    print('Categorias: ')
    ruta_categorias=Path(ruta)
    lista_categorias=[]
    contador=1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str=str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador+=1
    
    return lista_categorias

def elegir_categorias(lista):
    eleccion_categoria='x'

    while not eleccion_categoria.isnumeric() or int(eleccion_categoria) not in range(1, len(lista)+1):
        eleccion_categoria=input('\nElige una Categoria: ')

    return lista[int(eleccion_categoria) - 1]

def mostrar_receta(ruta):
    print('Recetas: ')
    ruta_recetas= Path(ruta)
    lista_recetas=[]
    contador=1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str=str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(receta)
        contador+=1

    return lista_recetas

def elegir_receta(lista):
    eleccion_receta='x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1,len(lista)+1):
        eleccion_receta=input('\nElige una receta: ')
    return lista[int(eleccion_receta)-1]

def leer_receta(receta):
    print('La receta es: ')
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe=False
    while not existe:
        print('Escribe el nombre de la receta: ')
        nombre_receta=input()+'.txt'
        print('Escribe tu nueva receta: ')
        contenido_receta=input()

        ruta_nueva = Path(ruta,nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva,contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe=True
        else:
            print('Esa receta ya existe')

def crear_categoria(ruta):
    existe=False
    while not existe:
        print('Escribe el nombre de la categoria: ')
        nombre_categoria=input()
        ruta_nueva = Path(ruta,nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu nueva categoria {nombre_categoria} ha sido creada')
            existe=True
        else:
            print('Esa categoria ya existe')

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada')

def eliminar_categoria(categoria):
    try:
        Path(categoria).rmdir()
        print(f'La categoria {categoria.name} ha sido eliminada')
    except Exception as error:
        print(error)

def volver_inicio():

    eleccion_inicio='x'
    while eleccion_inicio.lower() != 'v':
        eleccion_inicio=input('\nPresione V para volver al menu: ')


finalizar_programa=False
while not finalizar_programa:

    menu=inicio()

    if menu==1:
        mis_categorias=mostrarCategoria(mi_ruta)
        mi_categoria=elegir_categorias(mis_categorias)
        mis_recetas=mostrar_receta(mi_categoria)
        print('*'*4+'RECETA'+'*'*4)
        mi_receta=elegir_receta(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
    elif menu==2:
        mis_categorias=mostrarCategoria(mi_ruta)
        mi_categoria=elegir_categorias(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu==3:
        crear_categoria(mi_ruta)
        volver_inicio()
    elif menu==4:
        mis_categorias=mostrarCategoria(mi_ruta)
        mi_categoria=elegir_categorias(mis_categorias)
        mis_recetas=mostrar_receta(mi_categoria)
        mi_receta=elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu==5:
        mis_categorias=mostrarCategoria(mi_ruta)
        mi_categoria=elegir_categorias(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu==6:
        finalizar_programa=True
