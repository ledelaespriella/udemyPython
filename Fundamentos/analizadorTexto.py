'''Analizador de texto'''

text=input('Por favor ingrese un texto: ').lower()
print('Ahora ingrese 3 letras a su elección:')
a=input('Letra 1: ').lower()
b=input('Letra 2: ').lower()
c=input('Letra 3: ').lower()

lista= [a,b,c]
analisis1= [text.count(lista[0]),text.count(lista[1]),text.count(lista[2])]
analisis2= len(text.split())
analisis3= [text[0],text[-1]]
palabras=text.split()
palabras.reverse()

analisis4 = ' '.join(palabras)
result5 = 'python' in text

analisis5 = {True:'La palabra python se encuentra en el mensaje', False: 'La palabra python no se encuentra el mensaje'}


print('Analisis 1')
print(f'La letra {a} aparece {analisis1[0]} veces, la letra {b} aparece {analisis1[1]} veces y la letra {c} aparece {analisis1[2]}\n')

print('Analisis 2')
print(f'En el texto hay {analisis2} palabras\n')

print('Analisis 3')
print(f'La primera letra del texto es {analisis3[0]} y la ultima es {analisis3[1]}\n')

print('Analisis 4')
print(f'Palabras en orden inverso: {analisis4}\n')

print('Analisis 5')
print(analisis5[result5])

