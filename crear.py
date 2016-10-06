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


def salir():
    """
    Salir del script.
    TODO: Capturar SIGINT con el módulo signal y mostrar texto al salir.
    """
    raise SystemExit()


try:
    from jinja2 import Template, Environment, meta
except ImportError:
    print("No se ha podido importar jinja2")
    salir()


# Carga de archivo(s) plantilla.
# Asignación de valores a variables. (con opción por defecto)
#     Basar opción por defecto en el entorno en el que se ejecuta.
#
class Plantilla():
    """
    A partir de un archivo plantilla en el que existen $variables.
    """

    def _get_vars(self, path):
        """
        Dada la ruta de una plantilla, extraer todas sus variables para poder
        pasárselas luego.
            @path: ruta del archivo relativa a este script.
            returns:
                variables - Un diccionario con las variables como claves
                            (sin valores asignados, a priori)
        """
        entorno = Environment()
        arbol_de_sintaxis = entorno.parse(open(path).read())
        variables = meta.find_undeclared_variables(arbol_de_sintaxis)
        return variables

    def __init__(self, template_path):
        # Abrir archivo
        self.template = Template(open(template_path).read())
        self.variables = self._get_vars(template_path)

    def __str__(self):
        return str(self.template)

    def safe_substitute(self, valores={}):
        """
        Sustituye los tokens de la plantilla, intentando evitar excepciones.
        """
        return self.archivo.safe_substitute(valores)


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


def folderTree(path):
    """
    Dada una ruta a través de path, crear la estructura de directorios de un
    módulo básico.
    """
    if type(path) != str:
        path = str(path)
    if not path.startswith('/'):
        print("La ruta no es relativa, calculando ruta absoluta...")
        path = os.path.abspath(path)
    if not os.path.isdir(path):
        print('La ruta proporcionada ({0}) no existe.'.format(path))
        salir()
    else:
        if path.endswith('/'):
            path.rstrip('/')
    nombre_del_modulo = input('Introduce el nombre del módulo a crear: ')
    ruta_modulo = '/'.join((path, nombre_del_modulo))
    os.makedirs(ruta_modulo)
    os.makedirs('/'.join((ruta_modulo, 'models')))
    os.makedirs('/'.join((ruta_modulo, 'views')))


def newModule():
    """
    Crear un nuevo módulo a partir de plantillas básicas.
    """
    n = False
    ruta = input("Introduce la ruta donde se creará el módulo [./]: ") or './'
    folderTree(ruta)
    rellenarPlantilla(nombre="README", ruta='templates/README.rst')
    while type(n) != int:
        n = input("Cuántos modelos quieres crear? ")
        try:
            n = int(n)
        except ValueError:
            print("¡Introduce un número!")
    for n in range(n):
        rellenarPlantilla(
            nombre="módulo",
            ruta='templates/models/model_template.py')


def modificarVariable(variables, nombre):
    """
    Dado un diccionario de variables, modificar el valor de una de ellas.
    """
    variables.update({
                    nombre: input(
                            "Introduce un nuevo valor para {0}".format(nombre)
                        )
                    }
                    )
    return variables


def rellenarPlantilla(ruta, nombre='plantilla'):
    """
    Dada la ruta de una plantilla, esta función la rellena consultando al
    usuario.
        @ruta: cadena con la ruta de la plantilla, absoluta o relativa.
    """
    os.system('clear')
    print("Rellenar {0}".format(nombre))
    # TODO: Mostrar el nombre de la plantilla en la primera línea del terminal
    #       para saber qué estamos haciendo.
    # TODO: meter resto de plantillas, mejor en un bucle que llame a esta
    #       función
    plantilla = Plantilla(ruta)
    # Consultar datos
    # TODO: Tener valores por defecto.
    variables = {}
    for token in plantilla.variables:
        variables.update(
            {
                token: input(
                        "Introduce un valor para {0}:".format(token))
            }
            )
    print("Este es el archivo que se va a crear: {0}".format(
                                        plantilla.template.render(variables)))
    validacion = input('¿Es correcto? (Sí/No)[S]: ')
    # TODO: Si no se valida el archivo, ofrecer una lista de variables y
    # corregir la que toque.
    if validacion.lower() == 's':
        return plantilla.template.render(variables)
    elif validacion.lower() == 'n':
        # Mostrar lista de las variables:
        # claves = list(variables.keys())
        # menu(nombre="para corregir variables", opciones={
                                        # claves.index(
                                            # variable): {
                                            # 'nombre': str(variable),
                                            # 'funct': modificarVariable,
                                            # 'param': {
                                                # 'variables': variables,
                                                # 'nombre': str(variable)
                                            # }}
                                        # for variable, valor in variables
                                                        # })
        pass
    else:
        print("Respuesta no válida")


def opcion2():
    print("Opción 2!")


def opcion3():
    print("Opción 3!")


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


def menu(nombre="principal", opciones=opciones_principal, parametros={}):
    """
    Menú
        @nombre: nombre del menú para mostrarlo en la interfaz.
        @opciones: diccionario en el que las claves son el número
                    del menú y los valores son otro diccionario fomrado por:
                        nombre: nombre a mostrar en el menú.
                        funct: función (callable) a llamar.
                        param: diccionario de parámetros a pasar a
                                la función.
    """
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
        # pasar = parametros or opciones[opcion]['param']
        # if pasar: opciones[opcion]['funct'](**pasar)
        # else: opciones[opcion]['funct']()
        opciones[opcion]['funct']()
    except ValueError:
        print("Opción inválida")
        sleep(1)
        menu(nombre, opciones, parametros)
    except KeyError:
        print("Opción no válida")
        sleep(1)
        menu(nombre, opciones, parametros)

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
    while True:
        menu()
