import os

class Persona():
    def __init__(self,nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido

    def setApellido(self,apellido):
        self.__apellido =apellido
    
class Client(Persona):

    def __init__(self,nombre, apellido,numeroCuenta,balance=0):
        super().__init__(nombre, apellido)
        self.__numeroCuenta = numeroCuenta
        self.__balance = balance
    
    def getNumeroCuenta(self):
        return self.__numeroCuenta

    def getBalance(self):
        return self.__balance

    def setBalance(self,cantidad):
        self.__balance = cantidad

    def __str__(self):
        return f'Nombre: {self.getNombre()}\nApellido: {self.getApellido()}\nNumero de cuenta: {self.getNumeroCuenta()}\nBalance: {self.getBalance()}'

    def depositar(self,cantidad):
        saldo=self.getBalance()+cantidad
        self.setBalance(saldo)

        print(f'El saldo actual  es {self.getBalance()}')

    def retirar(self,cantidad):
        saldo=self.getBalance()-cantidad
        if saldo<0:
            print('No tiene saldo suficiente en la cuenta para poder retirar')
        else:
            self.setBalance(saldo)

        print(f'El saldo actual es {self.getBalance()}')

def verificarNumero():
    veri=True
    while veri:
        dato=input('Dato: ')
        try:
            dato=int(dato)
            res=True
        except ValueError as e:
            print(f'Error: No puede ingresar letras solo numeros')
            res=False
        if res!=False:
            return dato

def crear_cliente():
    print('Por favor ingrese los siguientes datos: \n')
    nombre=input('Nombre: ')
    apellido=input('Apellido: ')
    cuenta=input('Numero de cuenta: ')

    return Client(nombre,apellido,cuenta)

def inicio(cliente):
    os.system("clear")
    ver=True
    while ver:
        print(f'bienvenido Sus datos almacenados son los siguientes:\n{str(cliente)}')
        print("""¿Que desea hacer?
        
        [1]-Depositar
        [2]-Retirar
        [3]-salir""")
        opcion=verificarNumero()
        
        if opcion==1:
            print("¿Cuanto desea depositar?: \n")
            deposito=verificarNumero()
            cliente.depositar(deposito)
        elif opcion==2:
            print("¿Cuanto desea retirar?: \n")
            retiro=verificarNumero()
            cliente.retirar(retiro)
        elif opcion==3:
            ver=False
            os.system('clear')
            print('Gracias por utilizar el programa')
        else:
            print('Opcion incorrecta intente de nuevo')


print('Binevenido al programa para crear su cuenta bancaria')
cliente=crear_cliente()
inicio(cliente)






        
    

