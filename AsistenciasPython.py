# Ejercicios: octubre 2022


# Ejercicio Renzo Viscio
# Ejercicio 11: Agenda telefónica

agenda = {}
while True:
    print('\t.:MENU:.')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    print('5. Vaciar agenda de contactos')
    opcion = int(input('Digite una opción del menú: '))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el número de teléfono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('¡Contacto agregado exitosamente!')
        else:
            print('Este nombre de contacto ya existe')
    elif opcion == 2:
        nombre = input('¿Cuál es el nombre del contacto?: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto')
        else:
            print('Este contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Teléfono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
    elif opcion == 5:
        agenda = {}
        break
    else:
        print('\nOpción incorrecta')
    print()
    
    
    #Ejercicio EMIR MAYA
    ##Ya había pasado mi ejercicio, pero voy a hacer el commit
    #Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
#Numericos, utilizando argumentos variables *args como parametro de la
# funcion y agregar como resultado la suma de todos los valores pasados
# como argumentos.

def sumar_valor(*args): #recibimos una cantidad de parametros indefinidos
    res = 0
    # Iteramos cada elemento
    for valor in args:
        res += valor
    return res
#Llamamos a la funcion
print(sumar_valor(3, 5, 9))

        # Ejercicio BIANCA TOSETTO
# Ejercicio Funciones 05: Convertidor de Temperaturas
# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa

# De celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * (9 / 5) + 32 # Precedencia de operacion: *, /, + (izq a der)

# De fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

celsius = float(input('Ingrese la temperatura en grados celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'La temperatura en grados fahrenheit es: {resultado}')

fahrenheit = float(input('Ingrese la temperatura en grados fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'La temperatura en grados celsius es: {resultado}')

# Soel Antonio Attala
# Ejercicio 4: calculadora de impuestos
# Crear una función para calcular el total de un pago, incluyendo un impuesto aplicado(IVA)

def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la función
pago_sin_impuesto = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')


class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'color = ' + self.color + '\nruedas = ' + str(self.ruedas)

#Gaston Franco    

#Ejercicio clase 11
# Herencia a otra clase
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + '\nvelocidad = ' + str(self.velocidad)



# Herencia a otra clase
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + '\ntipo = ' + self.tipo

# Objetos
vehiculo = Vehiculo('Rojo', 4)
auto = Auto('Rojo', 4, 120)
bici = Bicicleta('negra', 2, 'playera')


