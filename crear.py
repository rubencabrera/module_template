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


# Carga de archivo(s) plantilla.
# Asignación de valores a variables. (con opción por defecto)
#     Basar opción por defecto en el entorno en el que se ejecuta.
#


def opcion1():
    """
    Opción 1
    """
    return print("Opción 1!")


def opcion2():
    print("Opción 2!")


def opcion3():
    print("Opción 3!")


def salir():
    raise SystemExit()


# Pantalla de bienvenida. Menú de opciones.


opciones_principal = {
    1: {
        'nombre':'uno',
        'funct': opcion1,
       },
    2:  {
        'nombre':'dos',
        'funct': opcion2,
       },
    3: {
        'nombre':'tres',
        'funct': opcion3,
    },
    0: {
        'nombre':'Salir',
        'funct': salir,
    },
}

def menu(nombre="principal",opciones=opciones_principal):
    """Menú principal"""
    os.system('clear')
    print("Esto es el menú {0}".format(nombre))
    print("""
          1) Opción 1
          2) Opción 2
          3) Opción 3
          0) Salir
          """)
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
