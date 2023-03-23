from reg import evaluar
from Thompson import thompson, grafo, alfabeto, simular
from Errores import *
from AFD_Converter import *
from SintaxT import *
import re

expresiones_reg = []

# Abriendo el archivo expresiones.yal para leer su contenido.
with open("expresiones.yal", "r") as file:
    data = file.read() # Leyendo la data del archivo.
    
    print("Data: ", data)

    # Expresión regular para encontrar las variables que se declaran con let.
    regex_let = r"let (\w+) = (.*)"

    # Encontrando las variables que se declaran con let.
    variables = re.findall(regex_let, data)

    print("Variables: ", variables)

    # Almacenando el contenido de las variables.
    expresiones_reg = [var[1] for var in variables]
    
    # Cambiando los [] por () en cada expresión regular de la lista de expresiones_reg.
    for i in range(len(expresiones_reg)):
        expresiones_reg[i] = expresiones_reg[i].replace("[", "(")
        expresiones_reg[i] = expresiones_reg[i].replace("]", ")")
    
    print("Expresiones regulares: ", expresiones_reg)

inp = input("Ingrese la expresion regular: ")


# Recorriendo la expresión regular para verificar si hay un ? para cambiarlo por un a|ε.
if "?" in inp:
    inp = inp.replace("?", "|ε")

# Recorriendo la expresión regular para hacer la idempotencia de la cerradura de Kleene (o sea si hubiera un a**** cambiarlo a a*)
if "*" in inp:
    inp = inp.replace("*****************", "*")
    inp = inp.replace("****************", "*")
    inp = inp.replace("***************", "*")
    inp = inp.replace("**************", "*")
    inp = inp.replace("************", "*")
    inp = inp.replace("**********", "*")
    inp = inp.replace("********", "*")
    inp = inp.replace("******", "*")
    inp = inp.replace("*****", "*")
    inp = inp.replace("****", "*")
    inp = inp.replace("***", "*")
    inp = inp.replace("**", "*")

verificacion = deteccion(inp) # Verificando que la expresión regular sea correcta.

if verificacion == True: # Si la expresión regular es correcta, se procede a evaluarla.
    
    regex = evaluar(inp)
    alfabeth = alfabeto(regex)
    print("La expresion regular es correcta.")
    print("La expresion regular es: ", regex)
    automata, lista, diccionario = thompson(regex) # Creando el AFN.

    #graficar(automata, lista, diccionario)
    grafo(automata, lista, diccionario) # Graficando el AFN.
    
    # Simulando el AFN.
    simular(automata,diccionario)

    # Haciendo la conversión a AFD.
    AFD(alfabeth, automata, lista, diccionario)

    # Haciendo la conversión a AFD directo.
    SintaxT(regex, alfabeth)
    
else:
    print("La expresion regular es incorrecta.")
