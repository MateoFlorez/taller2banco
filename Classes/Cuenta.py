class Cuenta:

    def __init__(self):
        self.__numeroCuenta = None
        self.__saldo = None

    # GETTERS
    @property
    def numeroCuenta(self):
        return(self.__numeroCuenta)

    @property
    def saldo(self):
        return(self.__saldo)

    # SETTERS
    @numeroCuenta.setter
    def numeroCuenta(self,numeroCuenta):
        print('Digite el numero de cuenta: ')
        self.__numeroCuenta = int(input(numeroCuenta))

    @saldo.setter
    def saldo(self,saldo):
        print('Digite el saldo de la cuenta: ')
        self.__saldo = int(input(saldo))