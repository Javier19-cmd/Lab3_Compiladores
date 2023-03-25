from reg import evaluar
from Thompson import thompson, grafo, alfabeto, simular
from Errores import *
from AFD_Converter import *
from SintaxT import *
import re
from prettytable import PrettyTable

tabla = {}

# Abriendo el archivo expresiones.yal para leer su contenido.
with open("exp1.yal", "r") as file:
    data = file.read() # Leyendo la data del archivo.
    
    #print("Data: ", data)

    # Expresión regular para encontrar las variables que se declaran con let.
    regex_let = r"let (\w+) = (.*)"

    # Encontrando las variables que se declaran con let.
    variables = re.findall(regex_let, data)

    #print("Variables: ", variables)

    # Almacenando el nombre de las variables y su expresión regular en la tabla.
    for variable in variables:
        tabla[variable[0]] = variable[1]
    
    #print("Tabla: ", tabla)
    
    # Reemplazando el E por un epsilon.
    for key in tabla:
        tabla[key] = tabla[key].replace("E", "ε")
    
    #print("Tabla: ", tabla)

    # Reemplazos.

    # Letras.
    # Verificando que sí haya una definición de letras.
    if 'letter' in tabla:
        new_letters = '(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z)'
        tabla['letter'] = tabla['letter'].replace("['a'-'z' 'A'-'Z']", new_letters)
        #print("Tabla: ", tabla)

    # Números.
    # Verificando que sí haya una definición de números.
    if 'digit' in tabla:
        new_digits = '(0|1|2|3|4|5|6|7|8|9)'
        tabla['digit'] = tabla['digit'].replace("['0'-'9']", new_digits)
    
    
    # Verificando si hay una definición de digit+
    if 'digits' in tabla:
        new_digitsp = '(0|1|2|3|4|5|6|7|8|9)+'
        tabla['digits'] = tabla['digits'].replace("digit+", new_digitsp)
    
    #print("Tabla: ", tabla)

    # Verificando si hay una definición id.
    if 'id' in tabla:
        new_letters = '(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z)'
        new_digitsp = '(0|1|2|3|4|5|6|7|8|9)+'
        """
            El reemplazo sería: 
            id = letter (letter | digit)*
            en donde letter se cambia por new1_letters 
            y digits por new1_digitsp
        """

        tabla['id'] = tabla['id'].replace("letter", new_letters)
        tabla['id'] = tabla['id'].replace("digits", new_digitsp)
        
    #print("Tabla: ", tabla)

    # Verificando si hay una definición de number.
    if 'number' in tabla:
        new_digitsp = '(0|1|2|3|4|5|6|7|8|9)+'
        """
            El reemplazo sería:
            digits se cambia por new_digitsp.
        """

        tabla['number'] = tabla['number'].replace("digits", new_digitsp)
    
    #print("Tabla: ", tabla)

    # Verificando si existen corchetes para reemplazarlos con paréntesis.
    for key in tabla:
        tabla[key] = tabla[key].replace("[", "(")
        tabla[key] = tabla[key].replace("]", ")")
    
    #print("Tabla: ", tabla)

    # # Creando la tabla.
    # table = PrettyTable()
    # table.field_names = ["Variable", "Expresión regular"]

    # # Agregando los datos a la tabla.
    # for key in tabla:
    #     table.add_row([key, tabla[key]])
    
    # # Imprimiendo la tabla.
    # print(table)

    #print("Tabla: ", tabla)

    # Metiendo a una lista los valores del diccionario.
    lista = []
    for key in tabla:
        lista.append(tabla[key])
    
    #print("Lista: ", lista)

    regex = ""

    for elemento in lista: 
        # Haciendo un join con | de los elementos de la lista.
        regex = "|".join(lista)

    print("Regex: ", regex)