import re

# Clase para detectar errores.

def deteccion(regex):

    parent = check_parenthesis(regex)

    if not parent:
        print("Error: La expresión regular no tiene paréntesis consistentes.")
        return False

    # # Verificando que la expresión tenga paréntesis de apertura y cierre.
    # if regex.count('(') != regex.count(')'):
    #     print("Error: La expresión regular no tiene paréntesis de cierre.")
    #     return False
    
    # Verificando que la expresión tenga letras o números.
    coin = re.match(r"[a-zA-Z0-9ε]*", regex)

    if not coin:
        print("Error: La expresión regular no tiene letras o números.")
        #print("Error: La expresión regular no puede tener números y letras.")
        return False


    # Verificando que la expresión no tenga un * o un + al inicio.
    coincidencia = re.match(r"^(?![*+]).*", regex)

    if not coincidencia:
        print("Error: La expresión regular no puede empezar con un * o un +.")
        return False
    
    # Verificando que la expresión no tenga un | hasta el final.
    coincidencia = re.match(r".*(?<!\|)$", regex)

    if not coincidencia:
        print("Error: La expresión regular no puede tener un | suelto.")
        return False
    
    # # Verificando que la expresión tenga los paréntesis de apertura y cierre correctos.


    # if parent == 0:
    #     print("Error: La expresión no tiene consistencia en sus paréntesis.")
    #     return False

    # coincidenci = re.match(r"^(?![*+]).*", regex)

    # if not coincidenci:
    #     print("Error: La expresión no tiene consistencia en sus paréntesis.")
    #     return False
    
    # Verificando que la expresión no tenga un * o un + al final.

    # # Verificando que no hayan operadores diferentes a +, |, ., ?, *.
    # coincidencia = re.match(r"[a-zA-Z0-9ε*+|?.]*", regex)

    # if coincidencia:
    #     print("Error: La expresión regular tiene operadores diferentes a +, |, ., ?, *.")
    #     return False
    
    # # Verificando que no hayan letras o números diferentes a a-z, A-Z, 0-9.
    # coincidencia = re.match(r"[a-zA-Z0-9ε*+|?.]*", regex)
    # if coincidencia:
    #     print("Error: La expresión regular tiene letras o números diferentes a a-z, A-Z, 0-9.")
    #     return False
    
    # # Verificando si hay errores combinados como -a+, o (a* o )a|) o )+a(
    # coincidencia = re.match(r"^[a-zA-Z0-9ε*+|?.]*$", regex) 

    # if not coincidencia:
    #     print("Error: La expresión regular tiene errores combinados como -a+, o (a* o )a|) o )+a(")
    #     return False

    return True

def check_parenthesis(regex):
    stack = []
    for char in regex:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0