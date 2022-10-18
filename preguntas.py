"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


from typing import Counter
import itertools
from operator import itemgetter


def lectura_archivo():
    with open("data.csv", "r") as file:
        datos_1 = file.readlines()
    

    # Orden de datos
    datos_1 = [line.replace("\n", "") for line in datos_1]

    
    # de strings a listas
    
    datos_1 = [line.split("\t") for line in datos_1]
    

    return datos_1


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    
    """
    datos=lectura_archivo()
    suma=0
    respuesta=[int(z[1]) for z in datos]
    suma=sum(respuesta)
    return suma

pregunta_01()

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    datos=lectura_archivo()
    parejas = [(x[0]) for x in datos]
    parejas2=[]

    conteo=Counter(parejas)

    for key in sorted(conteo.keys()):
        parejas2.append((key,conteo[key]))

     
    return parejas2



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    datos=lectura_archivo()
    parejas = [(x[0],x[1]) for x in datos]
    suma={}
    for x in parejas:
        if x[0] in suma:
            suma[x[0]]+=int(x[1])
        else:
            suma[x[0]]=int(x[1])
    
    resultado=[]

    for key in sorted(suma.keys()):
        resultado.append((key,suma[key]))
    return resultado



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    datos=lectura_archivo()
    #Selecionamos la fila
    #Se selecciona la columna de las fechas [1]
    #Se convierte en lista con split
    #Se selecciona el dato corresponde a mes
    meses = [x[2].split('-')[1] for x in datos]
    suma=Counter(meses)
    parejas2=[]
    for key in sorted(suma.keys()):
        parejas2.append((key,suma[key]))
    
    return parejas2


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
        #Leemos el archivo
    datos=lectura_archivo()

    datos=[(x[0],x[1])  for x in datos]
    
    resultado={}
    datos=sorted(datos)

    # Se agrupa las datos por tipo de llave
    for x in datos:
        if x[0] not in resultado.keys():
            resultado[x[0]]=x[1]
        else:
            resultado[x[0]]+=',' + x[1]

    #Se selecciona el valor mayor y menor de cada diccionario
    final=[]
    for x in resultado.keys():
        final.append((x,
                int(max(resultado[x].split(','))),
                int(min(resultado[x].split(',')))))
    return final

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    datos=lectura_archivo()

    datos=[x[4]  for x in datos]
    datos=[x.split(",") for x in datos]
    datos=[x for lista in datos for x in lista]
    datos=sorted(datos)
    datos=[x.split(":") for x in datos]

    # Se agrupa las datos por tipo de llave
    resultado={}
    
    for x in datos:        
        if x[0] not in resultado.keys():
            resultado[x[0]]=x[1]
        else:
            resultado[x[0]]+=',' + x[1]
    
    #Se selecciona el valor mayor y menor de cada diccionario
  
    
    final=[]
    for x in resultado.keys():

        #print(resultado[x].split)
        xxx=resultado[x].split(',')
        xxx=[int(x) for x in xxx]
        final.append((x,
                (min(xxx)),
                (max(xxx))))
    
    return final


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    datos=lectura_archivo()
    datos=[(x[1],x[0])  for x in datos]

    # Se agrupa las datos por tipo de llave
    resultado={}
    for x in datos:
        if x[0] not in resultado.keys():
            resultado[x[0]]=x[1]
        else:
            resultado[x[0]]+=',' + x[1]

    for x in resultado.keys():
        resultado[x]=resultado[x].split(',')

    #se quita las llaves y se deja como lista
    final=[]
    for i in resultado.keys():
        final.append((int(i),resultado[i]))

    final=sorted(final)

    return final



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    datos=lectura_archivo()
    datos=[(x[1],x[0])  for x in datos]

    # Se agrupa las datos por tipo de llave
    resultado={}
    for x in datos:
        if x[0] not in resultado.keys():
            resultado[x[0]]=x[1]
        else:
            resultado[x[0]]+=',' + x[1]

    for x in resultado.keys():
        resultado[x]=resultado[x].split(',')

    #se quita las llaves y se deja como lista
    final=[]

    for i in resultado.keys():
        #Se llama los valores
        #Se elimina repetidos con set
        #Se ordena con append
        #Se le asigna valor y se agrega a resultado
        final.append((int(i),sorted(list(set(resultado[i])))))

    final=sorted(final)

    return final



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    datos=lectura_archivo()
    datos=[x[4]  for x in datos]
    datos=[x.split(",") for x in datos]
    datos=[x for lista in datos for x in lista]
    datos=sorted(datos)
    datos=[x.split(":")[0] for x in datos]
    suma=Counter(datos)
    #Se creo un diccionario de conteo
    #Se transforma ese diccionario a la forma solicitada
    parejas2={}
    for key in sorted(suma.keys()):
        parejas2[key]=suma[key]
    return parejas2

pregunta_09()

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    datos=lectura_archivo()
    datos=[(x[0], len(x[3].split(',')), int(len(x[4].split(':')))-1)  for x in datos]
    print(datos)
    return datos



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    datos=lectura_archivo()
    datos=[[x[1], x[3].split(',')]  for x in datos]
    #se crea la duplas (letra, valor)
    datos=[(y, int(x[0])) for x in datos for y in x[1] ]
    datos=sorted(datos)
    #Se cuenta cada registro
    resultado={}
    for i in datos:
        if i[0] not in resultado.keys():
            resultado[i[0]]=i[1]
        else:
            resultado[i[0]]+=i[1]

    return resultado



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    datos=lectura_archivo()
    #creamos un lista que contega la columna 0 y 5
    #La columna 5 la ingresamos como una lista
    #['A', ['bbb:2', 'hhh:0', 'ccc:4', 'fff:1', 'aaa:7']]

    datos=[[x[0], x[4].split(',')]  for x in datos]
    datos=[(x[0],int(y.split(':')[1])) for x in datos for y in x[1]]
    #se crean las duplas (letra, valor)
    #datos=[(y, int(x[0])) for x in datos for y in x[1] ]
    #datos=sorted(datos)
  
    datos=sorted(datos)
    resultado={}
    for i in datos:
        if i[0] not in resultado.keys():
            resultado[i[0]]=i[1]
        else:
            resultado[i[0]]+=i[1]

    print(resultado)
    return resultado
