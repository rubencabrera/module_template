#! /usr/bin/python3
# -.- encoding: utf-8 -.-

# Asistente para crear módulos de odoo

###########################################################
# Autor: Rubén Cabrera Martínez
#        dev@rubencabrera.es
###########################################################

# Bloque de imports

import os
from time import sleep
from string import Template
import re


# Carga de archivo(s) plantilla.
# Asignación de valores a variables. (con opción por defecto)
#     Basar opción por defecto en el entorno en el que se ejecuta.
#
class Plantilla():
    """
    A partir de un archivo plantilla en el que existen $variables.
    """
    def __init__(self, plantilla):
        # Abrir archivo
        self.archivo = Template(open(plantilla).read())
        self.template = self.archivo.template

    def __str__(self):
        return self.template

    def safe_substitute(self, valores={}):
        """
        Sustituye los tokens de la plantilla, intentando evitar excepciones.
        """
        return self.archivo.safe_substitute(valores)

    def get_keys(self):
        """
        Devuelve una lista con las variables de la plantilla
        """
        # Obtener las variables de la plantilla
        resultado = re.findall(self.archivo.pattern, self.archivo.template)
        # Devuelve el segundo elemento de la tupla.
        return [r[1] for r in resultado]


def addField():
    """
    Crea una plantilla de módulo para añadir un campo.
    """
    # Nombre del modelo.
    # Nombre del campo.
    # Tipo de campo.
    #   Si es relacional: comodel_name...
    #
    print("Creando campo...")
    sleep(1)


def modulo():
    menu(
        nombre='crear módulo',
        opciones={
            1: {
                'nombre': "Módulo plantilla",
                'funct': newModule,
            },
            2: {
                'nombre': "Añadir Campo",
                'funct': addField,
            },
        }
    )


def newModule():
    """
    Crear un nuevo módulo a partir de plantillas básicas.
    """
    print("Crear nuevo módulo")
    # Carga de plantillas de archivos.
    # TODO: meter resto de plantillas
    plantillas = [
        Plantilla('README.rst'),
    ]
    # Consultar datos
    # TODO: Tener valores por defecto.
    for plant in plantillas:
        variables = {}
        for token in plant.get_keys():
            variables.update(
                {
                    token: input(
                            "Introduce un valor para {0}:".format(token))
                }
            )
        print("Esto es la plantilla:")
        print(plant.safe_substitute(variables))
        input()


def opcion2():
    print("Opción 2!")


def opcion3():
    print("Opción 3!")


def salir():
    raise SystemExit()


# Pantalla de bienvenida. Menú de opciones.


opciones_principal = {
    1: {
        'nombre': 'Crear módulo',
        'funct': modulo,
       },
    2:  {
        'nombre': 'dos',
        'funct': opcion2,
       },
    3: {
        'nombre': 'tres',
        'funct': opcion3,
    },
}


def menu(nombre="principal", opciones=opciones_principal):
    """Menú principal"""
    os.system('clear')
    opciones.update(
        {
            0: {
                'nombre': 'Salir',
                'funct': salir,
            },
        }
        )
    print("Esto es el menú {0}".format(nombre))
    for opt, dict_opt in opciones.items():
        print("{num}) {name}".format(num=str(opt), name=dict_opt['nombre']))
    try:
        opcion = int(input("Introduce una opción [0]:"))
        opciones[opcion]['funct']()
    except ValueError:
        print("Opción inválida")
        sleep(1)
        menu()
    except KeyError:
        print("Opción no válida")
        sleep(1)
        menu()
    menu()

# Opciones:

# Módulo para añadir campo(s)
#   Nombre del modelo.
#   Nombre del campo.
# Módulo para añadir vista(s)
#   Vista heredada.
#     Vista de la que se hereda.
#     Modelo.
#   Nueva vista.
#     Tipo de vista
# Módulo para añadir informe(s)
#   Modelo del informe.


if __name__ == '__main__':
    menu()
