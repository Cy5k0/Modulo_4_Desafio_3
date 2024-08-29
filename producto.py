class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

#metodos getter nombre, precio, stock
    #@property
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock


#metodos setter para stock con validacion para que no sea stock negativo

    def set_stock(self, valor):
        self.validar_stock(valor)
        self.__stock = valor



# FUNCIONES DE VALIDACION (las hice y no se si se vayan a usar al menos de esta forma)
    def validar_nombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena de caracteres")
    
    def validar_precio(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El precio debe ser un entero positivo")
        
    def validar_stock(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El stock debe ser un entero positivo")

