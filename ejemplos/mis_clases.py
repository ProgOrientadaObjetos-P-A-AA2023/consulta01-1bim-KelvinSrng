"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Universidad:
    
    def __init__(self, nombre, centrosDeportivos, centrosComida):
        self.nombre= nombre
        self.centrosDeportivos = centrosDeportivos
        self.centrosComida = centrosComida
        
    def __str__(self):
        return f"La {self.nombre} tiene {self.centrosDeportivos} centros deportivos y {self.centrosComida} centros de comida."

# clase 02
class Alumno:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def __str__(self):
        return f"El nombre del alumno es {self.nombre} y su apellido es {self.apellido}."