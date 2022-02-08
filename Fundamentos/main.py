#Trabajando con strings
from posixpath import split


mi_text="Mi nombre es, luis"
result=mi_text[::-1]
#print(result)

#metodos de un strings
upper= mi_text.upper()
print(f'texto en mayuscula {upper}')
lower= mi_text.lower()
print(f'texto en minuscula {lower}')
split= mi_text.split(' ')
print(f'texto separado en comas: {split}')
join=" ".join(split)
print(f'texto con join {join}')

"""Estoy haciendo una prueba de comentario"""

