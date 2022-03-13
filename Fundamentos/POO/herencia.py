class Animal:
    
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print('Este Animal ha nadico')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):
    
    def __init__(self,edad,color,altura):
        super().__init__(edad,color)
        self.altura = altura

    def hablar(self):
        print('Pio Pio')


piolin= Pajaro(4,'Azul',20)

# piolin.nacer()
# print(piolin.edad)


class Padre():
    def hablar(self):
        print('Hola')

class Madre():
    def reir(self):
        print('JAJAJAJA')

    def hablar(self):
        print('Que tal')

class Hijo(Madre,Padre):
    pass

class Nieto(Hijo):
    pass

nieto=Nieto()

nieto.hablar()
nieto.reir()

