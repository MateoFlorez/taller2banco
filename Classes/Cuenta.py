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
        self.__numeroCuenta = numeroCuenta

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo