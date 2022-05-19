from Classes.Cliente import Cliente
from Classes.Cuenta import Cuenta

# OBJETOS
cliente = Cliente()
cuenta = Cuenta()

clientes = []
cuentas = []

opcion = 1
nuevaOpcion = 1

# MENU
print('BANCO DE HIERRO ISLA BRAAVOS')
print('1. Agregar cliente')
print('2. Consultar estado de cuenta')
print('3. Ingresar / Retirar dinero')
print('4. Salir')

while (opcion != 4):
    opcion = int(input('Digita una opción: '))
    if(opcion == 1):
        cliente.nombre = input(f'Digite el nombre: ')
        cliente.apellido = input(f'Digite el apellido: ')
        cliente.cedula = int(input(f'Digite la cedula: '))
        cliente.ciudad = input(f'Digite la ciudad: ')
        cuenta.numeroCuenta = input(f'Digite el numero de cuenta: ')
        cuenta.saldo = input(f'Digite el saldo: ')

        clientes.append({"nombre":cliente.nombre,"apellido":cliente.apellido,"cedula":cliente.cedula,"ciudad":cliente.ciudad})
        cuentas.append({"numeroCuenta":cuenta.numeroCuenta,"saldo":cuenta.saldo})
        # clientes.append(cliente)
        # cuentas.append(cuenta)

    elif(opcion == 2):
        buscarCuenta = input('Digita la cuenta a buscar: ')

        print(next(x for x in cuentas if x["numeroCuenta"] == buscarCuenta))

        


    elif(opcion == 3):
        print('---- ESTADO DE CUENTA ----')
        buscarCuenta = input('Digita la cuenta a buscar: ')

        print(next(x for x in cuentas if x["numeroCuenta"] == buscarCuenta))
        print('----------------------------')
        print('¿Qué desea hacer?')
        print('1. Ingresar dinero')
        print('2. Retirar dinero')
        print('3. Volver al menú')

        while(nuevaOpcion != 3):
            saldoCuenta = int(cuenta.saldo)
            nuevaOpcion = int(input('Digita una opcion: '))
            if(nuevaOpcion == 1):
                print(f'Numero de cuenta: {cuenta.numeroCuenta}')
                print(f'Saldo: {cuenta.saldo}')
                ingreso = int(input('Dinero a ingresar: '))
                # saldoCuenta = saldoCuenta + ingreso
                cuenta.saldo = int(cuenta.saldo) + ingreso
                print(f'Tu nuevo saldo es de: {cuenta.saldo}')
                

            elif(nuevaOpcion == 2):
                print(f'Numero de cuenta: {cuenta.numeroCuenta}')
                print(f'Saldo: {cuenta.saldo}')
                retiro = int(input('Dinero a retirar: '))
                # saldoCuenta = saldoCuenta - retiro
                cuenta.saldo = int(cuenta.saldo) - retiro
                print(f'Tu nuevo saldo es de: {cuenta.saldo}')
            
            elif(opcion == 3):
                print('Saliendo del programa...')
            else:
                print('Digita una opción valida')
        else:
            print('Volviendo al Menu')
                

            
    
    elif (opcion == 4):
        print('Saliendo del programa...')
    else:
        print('Digita una opción valida')
