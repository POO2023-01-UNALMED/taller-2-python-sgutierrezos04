class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color):
        if color =="amarillo" or color =="rojo" or color =="verde" or color =="blanco" or color =="negro":
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        cantidadA = 0
        for asiento in self.asientos:
            if type(asiento) == Asiento:
                cantidadA += 1
        return cantidadA
    def verificarIntegridad(self):
        if self.motor.registro == self.registro:
            for asiento in self.asientos:
                if type(asiento) == Asiento:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if tipo == "gasolina" or tipo == "electrico":
            self.tipo = tipo