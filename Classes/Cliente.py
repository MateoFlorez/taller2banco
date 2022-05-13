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
        self.__nombre = input(f'Digite el nombre: {nombre}')

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = input(f'Digite el apellido: {apellido}')

    @cedula.setter
    def cedula(self,cedula):
        self.__cedula = int(input(f'Digite la cedula: {cedula}'))

    @ciudad.setter
    def ciudad(self,ciudad):
        self.__ciudad = input(f'Digite la ciudad: {ciudad}')