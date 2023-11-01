class MedioTransporte:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def presentar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
     

class Bicicleta(MedioTransporte):
    def __init__(self, marca, modelo):
        super().__init__("Bicicleta", marca, modelo)

class Moto(MedioTransporte):
    def __init__(self, marca, modelo):
        super().__init__("Moto", marca, modelo)

class Coche(MedioTransporte):
    def __init__(self, marca, modelo):
        super().__init__("Coche", marca, modelo)

class Autobus(MedioTransporte):
    def __init__(self, marca, modelo):
        super().__init__("Autobus", marca, modelo)

# Crear instancias de diferentes medios de transporte urbano
bicicleta = Bicicleta("Trek", "FX3")
coche = Coche("Toyota", "Corolla")
autobus = Autobus("Mercedes-Benz", "Citaro")
moto = Moto("Yamaha", "MT09")

# Presentar la información de cada medio de transporte
print("BIENVENIDO A MI PROGRAMA!!!")
x=0
while (x!=5 ):
    print("MENU:")
    print("1.PRESENTAR BICICLETA")
    print("2.PRESENTAR COCHE")
    print("3.PRESENTAR AUTOBUS")
    print("4.PRESENTAR MOTOCICLETA")
    print("5.SALIR")
    x= int(input("INGRESA UNA OPCION: "))
    if x==1:
        bicicleta.presentar_informacion()
        
    elif x==2:
        coche.presentar_informacion()
        
    elif x==3:
        autobus.presentar_informacion()

    elif x==4:
        moto.presentar_informacion()
        
    elif x==5:
        print("HASTA LUEGO :)")
        
    else :
        print("ERROR")
        


