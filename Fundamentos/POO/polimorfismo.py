import os

class Vaca():

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'{self.nombre} dice: Muu')

class Oveja():
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'{self.nombre} dice: Beee')

os.system('clear')
vaca1=Vaca('Aurora')
oveja1=Oveja('Nube')

animales=[vaca1,oveja1]

#en una iteracion se puede llamar el mismo metodo en objetos distintos
for animal in animales:
    animal.hablar()

def animal_habla(animal):
    animal.hablar()

print()
animal_habla(vaca1)
animal_habla(oveja1)