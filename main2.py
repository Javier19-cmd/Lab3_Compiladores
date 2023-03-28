from reg import evaluar
from Thompson import *
from Errores import *
from AFD_Converter import *
from SintaxT import *
import re

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

        # Si existe un str, o sea un (_)*, colocarlo también.
        if 'str' in tabla:
            tabla['id'] = tabla['id'].replace("str", tabla['str'])
        
    #print("Tabla: ", tabla)

    # Verificando si hay una definición de number.
    if 'number' in tabla:
        new_digitsp = '(0|1|2|3|4|5|6|7|8|9)+'
        new_signs = "@|~"
        """
            El reemplazo sería:
            digits se cambia por new_digitsp.
        """

        tabla['number'] = tabla['number'].replace("digits", new_digitsp)
        tabla['number'] = tabla['number'].replace("sign", new_signs)
    
    if 'sign' in tabla: 
        new_signs = "@|~"
        tabla['sign'] = tabla['sign'].replace("['+'|'-']", new_signs)

    
    # Leyendo el delim.
    if 'delim' in tabla:

        #print("Hay un delim")

        new_delims = "≡|¥|§"
        tabla['delim'] = tabla['delim'].replace("[' ''\\t''\\n']", new_delims)
    
    if 'ws' in tabla: 
        new_delims = "≡|¥|§"
        tabla['ws'] = tabla['ws'].replace("delim", new_delims)

        # Verificando como está el delim.
        # Si el delim está así [' ''\t''\n'], crear un or entre ellos.


    # print("Tabla: ", tabla)

    # Verificando si existen corchetes para reemplazarlos con paréntesis.
    for key in tabla:
        tabla[key] = tabla[key].replace("[", "(")
        tabla[key] = tabla[key].replace("]", ")")

    print("Tabla: ", tabla)

    # Metiendo a una lista los valores del diccionario.
    listaA = []

    listaF = []

    for key in tabla:
        listaA.append(tabla[key])
    
    #print("Lista: ", lista)

    # # Sacando cada regex para analizarla.
    # for regex in listaA:
    #     #print("Regex: ", regex)
    #     # Cambiando el ? por un |ε.
    #     regex = regex.replace("?", "|ε")

    #     # Simplificando los *.
    #     if "*" in regex:
    #         regex = regex.replace("*****************", "*")
    #         regex = regex.replace("****************", "*")
    #         regex = regex.replace("***************", "*")
    #         regex = regex.replace("**************", "*")
    #         regex = regex.replace("************", "*")
    #         regex = regex.replace("**********", "*")
    #         regex = regex.replace("********", "*")
    #         regex = regex.replace("******", "*")
    #         regex = regex.replace("*****", "*")
    #         regex = regex.replace("****", "*")
    #         regex = regex.replace("***", "*")
    #         regex = regex.replace("**", "*")

    #     #print("Regex: ", regex)

    #     # Quitando las comillas de los caracteres.
    #     regex = regex.replace("'", "")

    #     # # Haciendo el grafo.
    #     # grafo(automata, lista, diccionario)

    #     # Pasando a postfix.
    #     reg = evaluar(regex)

    #     #print("Regex: ", regex)

    #     listaF.append(reg)

    # #print("ListaF: ", listaF)

    # # Definiendo las listas para mandarlas a la unión de los AFNs.
    # automatasAFN = []
    # listasAFN = []
    # diccionariosAFN = []

    # # Por cada autómata de la listaF hacer un AFN.
    # for res in listaF:
    #     #print("Regex: ", res)

    #     # # Creando el AFN.
    #     automata, lista, diccionario = thompson(res)

    #     automatasAFN.append(automata)
    #     listasAFN.append(lista)
    #     diccionariosAFN.append(diccionario)

    
    # Uniendo los AFNs.
    #union_AFNs(automatasAFN, listasAFN, diccionariosAFN)

    #print("ListaA: ", listaA)

    # print("ListaF: ", listaF)

    regex_final = ""
    alf_final = ""
    lista_temp = []


    for i in range(len(listaA)):
        regex = listaA[i]
        regex = regex.replace("?", "|ε")

        if "*" in regex:
            regex = regex.replace("*****************", "*")
            regex = regex.replace("****************", "*")
            regex = regex.replace("***************", "*")
            regex = regex.replace("**************", "*")
            regex = regex.replace("************", "*")
            regex = regex.replace("**********", "*")
            regex = regex.replace("********", "*")
            regex = regex.replace("******", "*")
            regex = regex.replace("*****", "*")
            regex = regex.replace("****", "*")
            regex = regex.replace("***", "*")
            regex = regex.replace("**", "*")

        regex = regex.replace("'", "")
        listaA[i] = regex

        # Verificando que la expresión esté bien.
        bien = deteccion(regex)

        if bien: 

            # Obteniendo individualmente cada alfabeto.
            alfI = alfabeto(regex)

            # Pasando individualmente cada expresión a postfix.
            regexI = evaluar(regex)

            #print("RegexI: ", regexI)

            # Creando el AFD.
            #SintaxT(regexI, alfI)
        
        else: 
            print("Hubo un error con la regex")


    #print("ListaA: ", listaA)

    # Uniendo todas las expresiones mediante un |.
    expr = "|".join(listaA)

    #print("Expresión unida: ", expr)

    # Verificando que la expresión regular no tenga errores.
    bien = deteccion(expr)

    if bien:
    
        # Pasando a postfix.
        regex_final = evaluar(expr)

        #print("Expresión unida en postfix: ", regex_final)

        # Obteniendo alfabeto.
        alf_final = alfabeto(regex_final)

        SintaxT(regex_final, alf_final)
    
    else: 
        print("Hubo un error con la regex")