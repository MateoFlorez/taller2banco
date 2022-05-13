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
print('3. Ingresar o Retirar dinero')
print('4. Salir')

while (opcion != 4):
    opcion = int(input('Digita una opción: '))
    if(opcion == 1):
        cliente.nombre = ''
        cliente.apellido = ''
        cliente.cedula = 0
        cliente.ciudad = ''
        cuenta.numeroCuenta = 0
        cuenta.saldo = 0

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
                saldoCuenta = saldoCuenta + ingreso
                print(f'Tu nuevo saldo es de: {saldoCuenta}')
                

            elif(nuevaOpcion == 2):
                print(f'Numero de cuenta: {cuenta.numeroCuenta}')
                print(f'Saldo: {cuenta.saldo}')
                retiro = int(input('Dinero a retirar: '))
                saldoCuenta = saldoCuenta - retiro
                print(f'Tu nuevo saldo es de: {saldoCuenta}')
            
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
