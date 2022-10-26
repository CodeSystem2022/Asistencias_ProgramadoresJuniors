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

        # Ejercicio Bianca Tosetto
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
    
