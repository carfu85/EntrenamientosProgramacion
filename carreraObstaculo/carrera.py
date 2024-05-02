"""/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */"""
 

def carrera(atleta: list, pista:str)->bool:
    #Definicion de variables
    atleta = atleta
    pista = pista
    resultado= False
    carrera=[]
    i=0
    
    #Ciclo para recorrer la pista y 
    for piso in pista:
        accion= False 
        for step in atleta[i:len(atleta)]:
            if accion == False:
                if step == "run" and piso == "_":
                    carrera.extend("_")
                    accion = True
                    i +=1 #seguiente acción del atleta
                    next
                elif step == "jump" and piso == "|":
                    carrera.extend("|")
                    accion = True
                    i +=1
                    next
                elif step == "jump" and piso == "_":
                    carrera.extend("x")
                    accion = True
                    i +=1
                    next
                elif step == "run" and piso == "|":
                    carrera.extend("/")
                    accion = True
                    i +=1
                    next
                else:
                    print("Error")
            else:
                break
            
    for elemento in carrera:
        if elemento == "x" or elemento == "/":
            resultado = False
            break
        else:
            resultado = True
    
    if resultado == True:
        return print(f"Ha superado la carrera: {resultado}, Carrera: {carrera}")
        
    else:
        return print(f"No ha superado la carrera: {resultado}, Carrera: {carrera}")

# Test
atleta = ["run", "jump", "run", "jump", "run", "jump","jump","run"]
pista = "_|_|_|_|"
prueba = carrera(atleta, pista)