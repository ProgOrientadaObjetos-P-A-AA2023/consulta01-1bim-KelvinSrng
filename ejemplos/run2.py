"""

"""

from mis_clases import Universidad

# Crear dos objetos de la clase 02

# objeto 01

# crear

uni = Universidad("Universidad Tecnica Particular de Loja",3,2)

# Presentar objeto; usar el método __st__

print(uni)

# objeto 02

# crear ingresando valores por teclado

nombre = input("Ingrese el nombre de la institucion: ")
centrosD = input("Ingrese el numero de canchas: ")
centrosC = input("Ingrese el numero de centros de comida: ")

uni1 = Universidad(nombre,centrosD,centrosC)

# Presentar objeto; usar el método __st__

print(uni1)