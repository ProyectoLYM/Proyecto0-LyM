
def quitar_espacios(expresion):
    expresion = expresion.strip()
    return expresion


def cargar_archivo(archivo):
    contenido = open(archivo,"r").read()
    return contenido
    
    
print(cargar_archivo("ejemploFull.txt"))


def definicionVariable(linea):
    if "defVar" in linea:
        palabra = linea.split(" ")
        if "defVar" in palabra[0]:
            if len(palabra) == 3:
                primer_token = "Variable"
                segundo_token = "Nombre"
                tercer_token = "Valor"
                token = (primer_token,segundo_token,tercer_token)
            if len(palabra) > 3 or len(palabra) < 3:
                token = "No valido"
        else:
            token = "No valido"
    return token 
            

def definicionProceso(linea):
    if "defProc" in linea:
        palabra = linea.split(" ")
        if "defProc" in palabra[0]:
            if len(palabra[1] != 0):
                if "(" and ")" in linea:
                    parametros = linea.split("(")
                    parametro = parametros.split(",")
                    if parametro > linea.count(","):
                        token = ("Proceso", "Nombre", "Parametros")
                else:
                    token = "No valido"
            else:
                token = "No valido"
        else:
            token = "No valido"
    return token


def condicional(linea):
    if "if" in linea or "else" in linea:
            palabra = linea.split(" ")
            if "if" in palabra[0]:
                if "{" in linea or "{" in lineas[i + 1]:
                    
                    
def parser(contenido):
    respuesta1 = ""
    respuesta2 = ""
    respuesta3 = ""
    correcto = ""
    lineas = contenido.split("\n")
    for i in range(len(lineas)):
        linea = quitar_espacios(lineas[i])
    if definicionVariable(linea) == "Valido":
        respuesta1 = True
    else:
        respuesta1 = False
    if definicionProceso(linea) == "Valido":
        respuesta2 = True
    else:
        respuesta2 = False
    if condicional(linea) == "Valido":
        respuesta3 = True
    else:
        respuesta3 = False
    if respuesta1 and respuesta2 and respuesta3 == True:
        correcto = True
    else:
        correcto = False    
    return correcto 


def resultado(archivo):
    archivo = "ejemploFull.txt"
    carga = cargar_archivo(archivo)
    respuesta = parser(carga)
    if respuesta == True:
        res = print("La sintaxis es correcta: True")
    else:
        res = print("La sintaxis no es correcta: False")
    return res
    
    


def lexer(contenido):
    lineas = contenido.split("\n")
    tokens = []
    for i in range(len(lineas)):
        linea = quitar_espacios(lineas[i])
        if "defVar" in linea:
            palabra = linea.split(" ")
            if "defVar" in palabra[0]:
                if len(palabra) == 3:
                    primer_token = "Variable"
                    segundo_token = "Nombre"
                    tercer_token = "Valor"
                    token = (primer_token,segundo_token,tercer_token)
                if len(palabra) > 3 or len(palabra) < 3:
                    token = "No valido"
            else:
                 token = "No valido"  
        if "defProc" in linea:
            palabra = linea.split(" ")
            if "defProc" in palabra[0]:
                if len(palabra[1] != 0):
                    if "(" and ")" in linea:
                        parametros = linea.split("(")
                        parametro = parametros.split(",")
                        if parametro > linea.count(","):
                            token = ("Proceso", "Nombre", "Parametros")
                    else:
                        token = "No valido"
                else:
                    token = "No valido"
            else:
                token = "No valido"
        if "if" in linea or "else" in linea:
            palabra = linea.split(" ")
            if "if" in palabra[0]:
                if "{" in linea or "{" in lineas[i + 1]:
                    
                     
        tokens.append(token)
            
    return lista

    