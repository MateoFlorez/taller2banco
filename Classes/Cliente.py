class Cliente:

    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__cedula = None
        self.__ciudad = None

    # GETTERS
    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def apellido(self):
        return(self.__apellido)

    @property
    def cedula(self):
        return(self.__cedula)

    @property
    def ciudad(self):
        return(self.__ciudad)

    # SETTERS
    @nombre.setter
    def nombre(self,nombre):
        print('Digita el nombre: ')
        self.__nombre = input(nombre)

    @apellido.setter
    def apellido(self,apellido):
        print('Digita el apellido: ')
        self.__apellido = input(apellido)

    @cedula.setter
    def cedula(self,cedula):
        print('Digita la cedula: ')
        self.__cedula = int(input(cedula))

    @ciudad.setter
    def ciudad(self,ciudad):
        print('Digita la ciudad: ')
        self.__ciudad = input(ciudad)