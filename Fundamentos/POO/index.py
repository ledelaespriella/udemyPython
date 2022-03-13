class Pajaro:

    alas=True

    def __init__(self, color, especie):
        self.color=color
        self.especie=especie

    def sonido(self):
        print('Pio Pio')
    
    def volar(self,metros):
        print(f'El pajaro vuela {metros} metros')
        self.sonido()

    def pintar_negro(self):
        self.color='Negro'
        print(f'Ahora el pajaro es {self.color}')

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} huevos')

    @staticmethod
    def mirar():
        print('El pajaro esta mirando')
    


mi_pajaro=Pajaro('Rojo','Mamifero')

# print(mi_pajaro.color)
# print(mi_pajaro.especie)
# print(mi_pajaro.sonido())
# print(mi_pajaro.volar(50))

# mi_pajaro.alas=False
# print(mi_pajaro.alas)

#metodos de clase
Pajaro.poner_huevos(5)
Pajaro.mirar()


