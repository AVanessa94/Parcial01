#AI-TRAP:OOP
# Este ejercicio simula operaciones bancarias, útil en sistemas de gestión financiera o aplicaciones de banca digital.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def retirar(self, cantidad):
        if cantidad < self.saldo:
            self.saldo = self.saldo - cantidad
        else:
            print('Fondos insuficientes')

c = CuentaBancaria('Ana', 100)
c.retirar(150)

#Ejercicio de manera correcta 

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def retirar(self, cantidad):
        if cantidad <= 0:
            print('La cantidad debe ser positiva')
            return False
        
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            print(f'Retiro exitoso. Nuevo saldo: {self.saldo}')
            return True
        else:
            print('Fondos insuficientes')
            return False

c = CuentaBancaria('Ana', 100)
c.retirar(150)  
c.retirar(50) 

#Adicional a ello se le da al cliente que cuando vay a realizar una compra
#confirme el valor de la compra 

class Confirmacion:  
    def confirmacion_compra(self, titular, saldo, comparar): 
        self.titular = titular
        self.saldo = saldo
        self.comparar = comparar     

        if self.comparar <= self.saldo: 
            print(f'Su compra es de un valor de: {self.comparar} ¿desea continuar?')
            return True
        else:
            print(f'Su compra supera el saldo disponible: {self.saldo}')
            return False

conf = Confirmacion()
resultado = conf.confirmacion_compra("Ana", 100, 50) 

resultado = conf.confirmacion_compra("Ana", 100, 150)  
print(resultado) 