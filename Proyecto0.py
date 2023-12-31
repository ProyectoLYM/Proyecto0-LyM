archivo = input("Ingrese el nombre del archivo: ")


#La primera funciones para quitar los espacios de un str
def quitar_espacios(expresion):
    expresion = expresion.strip()
    palabras = expresion.split()
    espacio = " ".join(palabras)
    return espacio


#Aca cargamos el archivo, el cual puede estar en formato de csv o txt.
def cargar_archivo(archivo):
    contenido = open(archivo,"r").read()
    return contenido
    

#Esta funcion es para el lexer y se usa de manera que analice si las definiciones de variables estan sintacticamente correctas, retorna un token que puede ser Valido o No valido
def definicionVariable(linea):
    palabra = linea.split(" ")
    if "defVar" in palabra[0]:
        if len(palabra) == 3:
            token = "Valido"
        if len(palabra) > 3 or len(palabra) < 3:
            token = "No valido"
    else:
        token = "No valido"
    return token 
   
            
#Esta funcion es para el lexer y se usa de manera que analice si las definciones de procesos estan sintacticamente correctos, retorna un token que puede ser Valido o No valido
def definicionProceso(linea):
    palabra = linea.split(" ")
    if "defProc" in palabra[0]:
        if (palabra[1] != 0) == True:
            if "(" and ")" in linea:
                slice1 = linea.find("(")
                slice2 = linea.find(")")
                parametro = linea[slice1:slice2]
                parametros = parametro.split(",")
                if len(parametros) > parametro.count(","):
                    token = "Valido"
            else:
                token = "No valido"
        else:
            token = "No valido"
    else:
        token = "No valido"
    return token


#Esta funcion es para el lexer y se usa de manera que analice si los ifs(condicional) estan sintacticamente correctos, retorna un token que puede ser Valido o No valido
def condicionalif(lineas, i):
    linea = quitar_espacios(lineas[i])
    Encontro = False
    indice = i
    if "if" in linea:
            palabra = linea.split(" ")
            if "if" in palabra[0] or "}"in palabra[0]:
                if "{" in linea:
                    token = "Valido"
                else:
                    while (Encontro == False and indice < len(lineas)):
                        if "{" in lineas[indice]:
                            Encontro = True
                            token = "Valido"
                        elif "{" not in lineas[indice]:
                            Encontro = False
                            token = "No valido"
                        indice += 1
    return token


#Esta funcion es para el lexer y se usa de manera que analice si los elses(condicional) estan sintacticamente correctos, retorna un token que puede ser Valido o No valido
def condicionalelse(lineas, i):
    linea = quitar_espacios(lineas[i])
    Encontro = False
    indice = i
    if "else" in linea:
            palabra = linea.split(" ")
            if "else" in palabra[0] or "}" in palabra[0]: 
                if "{" in linea:
                    token = "Valido"
                else:
                    while (Encontro == False and indice < len(lineas)):
                        if "{" in lineas[indice]:
                            Encontro = True
                            token = "Valido"
                        elif "{" not in lineas[indice]:
                            Encontro = False
                            token = "No valido"
                        indice += 1
            else:
                token = "No valido"
    return token       
        
             
#Esta funcion es para el lexer y se usa de manera que analice si los whiles(ciclos) estan sintacticamente correctos, retorna un token que puede ser Valido o No valido
def ciclos(lineas, i):
    linea = quitar_espacios(lineas[i])
    encontro = False
    if "while" in linea:
        palabra = linea.split(" ")
        if "while" in palabra[0] or "}" in palabra[0]:
            if "{" in linea:
                token = "Valido"
            else:
                while (encontro == False and i < len(lineas)):
                    if "{" in lineas[i]:
                        encontro = True
                        token = "Valido"
                    elif "{" not in lineas[i] and len(lineas[i]) != 0:
                        encontro = False
                        token = "No valido"
                    i += 1
    return token
                          
        
#Esta funcion es para el lexer y se usa de manera que analice si hay una cantidad adecuada de ifs y elses, debido a que en ningun momento pueden haber mas ifs que elses
#retorna un token que puede ser Valido o No valido
def contarCondicionales(contenido):
    ifs = 0
    elses = 0
    invalido = False
    i = 0
    while i < len(contenido) and not invalido:
        if "if" in contenido[i]:
            ifs += 1
        if "else" in contenido[i]:
            elses += 1
            if elses > ifs:
                token = "No valido"
                invalido = True
            else:
                token = "Valido"
        i += 1
    return token


#Esta funcion es para el lexer y se usa de manera que analice si la cantidad de brackets que abren es igual a la cantidad de brackets que cierran.
#Analiza tambien que no exista ningun bracket cerrado sin antes haber uno abierto
def contarbrackets(contenido):
    centinela = True
    x = 0
    opbracket = 0
    clbracket = 0
    while(centinela and x < len(contenido)):
        if "{" in contenido[x]:
            opbracket += 1
        if "}" in contenido[x]:
            clbracket += 1 
        centinela = opbracket >= clbracket
        x += 1
    if centinela == True:
        token = "Valido"
    else:
        token == "Invalido"
    return token


#Esta funcion es para el lexer y se usa de manera que analice si la funcion Jump del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def funcionJump(linea):
    index = linea.find("jump")
    slice = linea[index:len(linea) + 1]
    if "(" in slice and ")" in slice:
        if slice.find("(") < slice.find(")"):
            token = "Valido"
        else:
            token = "No valido"
    else:
        token = "No valido" 
    return token 


#Esta funcion es para el lexer y se usa de manera que analice si la funcion Walk(sin valor) del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def funcionWalk(linea):
    index = linea.find("walk")
    slice = linea[index:len(linea) + 1]
    if "(" in slice and ")" in slice:
        if slice.find("(") < slice.find(")"):
            token = "Valido"
        else:
            token = "No valido"
    else:
        token = "No valido" 
    return token 
    
    
#Esta funcion es para el lexer y se usa de manera que analice si la funcion Walk(con valor) del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def funcionWalk2(linea):
    direccion = ["front", "right", "left", "back"]
    coord = ["north", "south", "west", "east"]
    index = linea.find("walk")
    for i in range(4):
        if direccion[i] in linea:
            lenght = len(direccion[i])
            index_value = linea.find(direccion[i])
        elif coord[i] in linea:
            lenght = len(coord[i])
            index_value = linea.find(coord[i])
        else:
            token = "No valido"
        slice = linea.replace(" ", "")
        slice1 = slice[index:index_value + lenght]
        if "(" in slice1 and ")" in slice1:
            if slice1.find("(") < slice1.find(")"):
                token = "Valido"
            else:
                token = "No valido"
        else:
            token = "No valido"
        return token
    
    
#Funcion walk para especificar si el walk tiene o no valor 
def walk(linea):
    spaces = linea.replace(" ", "")
    index = linea.find("walk")
    slice = linea[index:len(spaces) + 1]
    find1 = slice.find("(")
    find2 = slice.find(")")
    slice2 = slice[find1:find2 + 1]
    if "," in slice2:
        token = funcionWalk2(linea)
    else:
        token = funcionWalk(linea)
    return token
            

#Esta funcion es para el lexer y se usa de manera que analice si la funcion Leap(sin valor) del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def funcionLeap(linea):
    index = linea.find("leap")
    slice = linea[index:len(linea) + 1]
    if "(" in slice and ")" in slice:
        if slice.find("(") < slice.find(")"):
            token = "Valido"
        else:
            token = "No valido"
    else:
        token = "No valido" 
    return token         
            
            
def funcionLeap2(linea):
    direccion = ["front", "right", "left", "back"]
    coord = ["north", "south", "west", "east"]
    index = linea.find("leap")
    split = linea.split(";")
    for x in range(len(split)):
        if "leap" in split[x]:
            indice = x
    for i in range(4):
        if direccion[i] in split[indice]:
            lenght = len(direccion[i])
            index_value = split[indice].find(direccion[i])
            nuevo_index = split[indice].find("leap")
        elif coord[i] in split[indice]:
            lenght = len(coord[i])
            index_value = split[indice].find(coord[i])
            nuevo_index = split[indice].find("leap")
        else:
            token = "No valido"
        slice1 = split[indice].replace(" ", "")
        if "(" in slice1 and ")" in slice1:
            if slice1.find("(") < slice1.find(")"):
                token = "Valido"
            else:
                token = "No valido"
        else:
            token = "No valido"
        return token   
    

def leap(linea):
    spaces = linea.replace(" ", "")
    index = linea.find("leap")
    slice = linea[index:len(spaces) + 1]
    find1 = slice.find("(")
    find2 = slice.find(")")
    slice2 = slice[find1:find2 + 1]
    if "," in slice2:
        token = funcionLeap2(linea)
    else:
        token = funcionLeap(linea)
    return token 
    
#Esta funcion es para el lexer y se usa de manera que analice si la funcion turn del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def turn(linea):
    lista = ["left", "right", "around"]
    indice = linea.find("turn")
    param = 0
    for i in range(3):
        if lista[i] in linea:
            param = linea.find(lista[i]) + len(lista[i])
        else:
            token = "No valido"
    if param != 0:
        palabra = linea.replace(" ", "")
        indice = palabra.find("turn")
        palabra = palabra[indice:param + 1]
        if "(" in palabra and ")" in palabra:
            if palabra.find("(") < palabra.find(")"):
                token = "Valido"
            else:
                token = "No valido"
        else: 
            token = "No valido"
    else:
        token = "No valido"
    return token


#Esta funcion es para el lexer y se usa de manera que analice si la funcion turnto del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def turnto(linea):
    lista = ["north", "south", "east", "west"]
    param = 0
    for i in range(4):
        if lista[i] in linea:
            param = linea.find(lista[i]) + len(lista[i])
        else:
            token = "No valido"
    if param != 0:
        palabra = linea.replace(" ", "")
        indice = palabra.find("turnto")
        palabra = palabra[indice:param + 1]
        if "(" in palabra and ")" in palabra:
            if palabra.find("(") < palabra.find(")"):
                token = "Valido"
            else:
                token = "No valido"
        else: 
            token = "No valido"
    else:
        token = "No valido"
    return token


#Funcion para saber si un valor string puede ser convertido a entero(Se usa para saber si los parametros son enteros), retorna True o False
def es_entero(texto):
    try:
        int(texto)
        return True
    except ValueError:
        return False


#Esta funcion es para el lexer y se usa de manera que analice si la funcion drop del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def drop(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find("drop")
    if "(" in palabra and ")" in palabra:
        param = palabra.find("(")
        param2 = palabra.find(")")
        palabra = palabra[param + 1:param2]
    else:
        token = "No valido"
    if es_entero(palabra) == True:
        token = "Valido"
    else:
        token = "No valido"
    return token


#Esta funcion es para el lexer y se usa de manera que analice si la funcion get del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def get(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find("get")
    palabra1 = linea[indice:len(palabra) - 1]
    if "(" in palabra and ")" in palabra:
        param = palabra.find("(")
        param2 = palabra.find(")")
        palabra = palabra[param + 1:param2]
    else:
        token = "No valido"
    if es_entero(palabra) == True:
        token = "Valido"
    else:
        token = "No valido"
    return token


#Esta funcion es para el lexer y se usa de manera que analice si la funcion grab del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def grab(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find("grab")
    palabra1 = linea[indice:len(palabra) - 1]
    if "(" in palabra and ")" in palabra:
        param = palabra.find("(")
        param2 = palabra.find(")")
        palabra = palabra[param + 1:param2]
    else:
        token = "No valido"
    if es_entero(palabra) == True:
        token = "Valido"
    else:
        token = "No valido"
    return token


#Esta funcion es para el lexer y se usa de manera que analice si la funcion letGo del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def letGo(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find("letgo")
    palabra1 = linea[indice:len(palabra)]
    if "(" in palabra and ")" in palabra:
        param = palabra.find("(")
        param2 = palabra.find(")")
        palabra = palabra[param + 1:param2]
    else:
        token = "No valido"
    if es_entero(palabra) == True:
        token = "Valido"
    else:
        token = "No valido"
    return token


#Esta funcion es para el lexer y se usa de manera que analice si la funcion nop del programa esta sintacticamente correcta, retorna un token que puede ser Valido o No valido
def nop(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find("nop")
    palabra = linea[indice:indice+5]
    if "(" in palabra and ")" in palabra:
        token = "Valido"
    else:
        token = "No valido"
    return token

    
#El parser que analiza el lexer para saber si el programa esta sintacticamente correcto, Retorna True o False
def parser(tokens):
    correcto = True
    i = 0
    while(correcto and i < len(tokens)):
        if tokens[i] != "Valido":
            correcto = False
        else:
            i += 1
    return correcto

            
#El lexer que va analizando linea por linea el programa que se le ingrece y va a retornar una lista con tokens
def lexer(contenido):
    lineas = contenido.split("\n")
    tokens = []
    tokenbrackets = contarbrackets(contenido)
    tokencondicionales = contarCondicionales(lineas)
    tokens.append(tokenbrackets)
    tokens.append(tokencondicionales)
    for i in range(len(lineas)):
        linea = quitar_espacios(lineas[i])
        #print(linea)
        if "defVar" in linea:
            token = definicionVariable(linea)
            tokens.append(token)
        if "defProc" in linea:
            token = definicionProceso(linea)
            tokens.append(token)
        if "if" in linea:
            token = condicionalif(lineas, i)
            tokens.append(token)
        if "else" in linea:
            token = condicionalelse(lineas, i)
            tokens.append(token)
        if "while" in linea:
            token = ciclos(lineas, i) 
            tokens.append(token)
        if "walk" in linea:
            token = walk(linea)
            tokens.append(token)
        if "leap" in linea:
            token = leap(linea)
            tokens.append(token)
        if "jump" in linea:
            token = funcionJump(linea)
            tokens.append(token)
        if "turn" in linea and "turnto" not in linea:
            token = turn(linea)
            tokens.append(token)
        if "turnto" in linea:
            token = turnto(linea)
            tokens.append(token)
        if "nop" in linea:
            token = nop(linea)
            tokens.append(token) 
        if "drop" in linea:
            token = drop(linea)
            tokens.append(token)
        if "get" in linea:
            token = get(linea)
            tokens.append(token)
        if "grab" in linea:
            token = grab(linea)
            tokens.append(token)
        if "letgo" in linea:
            token = letGo(linea)
            tokens.append(token)
        else:
            token = None
    return tokens


#El resultado, para saber si la sintaxis del Archivo fue correcta
def resultado(archivo):
    carga = cargar_archivo(archivo)
    tokens = lexer(carga)
    #print(tokens)
    respuesta = parser(tokens)
    if respuesta == True:
        res = print("La sintaxis es correcta: True")
    else:
        res = print("La sintaxis no es correcta: False")
    return res

print(resultado(archivo))

