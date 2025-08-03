#######################################
# Empaquetado
#######################################
# - Módulo: archivo python (.py)
# - Paquete: colección de módulos (carpeta)

# Módulo
#######################################
# import nombreModulo [as alias]
# from nombreModulo import elemento [, elemento 2, ...]
# from nombreModulo import elemento as alias

# nombreModulo.elemento # Para acceder a funcionalidades o variables
# alias.elemento # Para acceder a funcionalidades o variables

#######################################

import input_utils # as utils

edad = input_utils.InputUtils.leerEnteroPositivo('Ingrese la edad: ')
print(edad)


from input_utils import InputUtils

edad = InputUtils.leerEnteroPositivo('Ingrese la edad: ')
print(edad)

# Paquete
#######################################
# /
# |--- main.py
# |--- utils
#     |--- __init__.py
#     |--- input_utils.py

# import utils.nombreModulo [as alias]
# from utils.nombreModulo import elemento [, elemento 2, ...]
# from utils.nombreModulo import elemento as alias

#######################################

import utils.input_utils # as utils

edad = utils.input_utils.InputUtils.leerEnteroPositivo('Ingrese la edad: ')
print(edad)


from utils.input_utils import InputUtils

edad = InputUtils.leerEnteroPositivo('Ingrese la edad: ')
print(edad)
