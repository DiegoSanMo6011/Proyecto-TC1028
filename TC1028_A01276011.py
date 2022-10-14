"""
Proyecto TC1028 "Mates Utiles y bonitas :)"
Calculadora de: teorema de pitagoras, regla de tres, formula general y caida libre
El programa pregunta la formula o formulas que necesita oucpar el usuario y le pide los datos necesarios para
resolverla, devuelve la lista de resultados.
"""
#bibliotecas
import math

"""
================== funciones formulas  =====================================
"""

#funciones pitagoras
def pitagorascateto(hipo,cateto_1):
    """
    (uso de operadores, uso de funciones)
    recibe: hipo valor numérico, cateto_1 valor numérico
    Aplica teorema  de pitagoras.
    devuelve: resultado de operación numérico (cateto).
    """
    cateto_2=math.sqrt(hipo**2-cateto_1**2)
    return cateto_2
def pitagorashipo(cateto_1,cateto_2):
    """
    (uso de operadores, uso de funciones)
    recibe: cateto_1 valor numérico, cateto_2 valor numérico
    Aplica teorema  de pitagoras.
    devuelve: resultado de operación numérico (hipotenusa).
    """
    hipo= math.sqrt(cateto_1**2+cateto_2**2)
    return hipo

#funcion regla de tres
def regla_de_tres(variable_comp,constante_inc,constante_comp):
    """
    (uso de operadores, uso de funciones)
    recibe: variable_comp valor numérico, constante_inc valor numérico y 
        constante_comp valor numérico.
    Divide al producto de variable_comp y constante_inc entre la constante_comp
    devuelve: resultado de operación numérico 
    """  
    resp=(variable_comp*constante_inc)/constante_comp
    return resp

#funcion formula general
def fromula_gene(a,b,c):
    """
    (uso de operadores, uso de funciones)
    recibe: a valor numérico,b valor numérico y 
        c valor numérico.
    Aplica formula general
    devuelve: resultado de operación numérico 
    """  
    if a!= 0:
        incognita_1=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
        incognita_2=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)
        incognitas.append(incognita_1)
        incognitas.append(incognita_2)
        return incognitas
    else:
        return "El valor de a no puede ser 0"

#funciones caida libre 
def caida_altura(t,g):
    """
    (uso de operadores, uso de funciones)
    recibe: t valor numérico y 
        g valor numérico.
    multiplica 1/2g por t^2
    devuelve: resultado de operación numérico 
    """  
    h=1/2*g*t**2
    return h
def caida_velfinh(h,g):
    """
    (uso de operadores, uso de funciones)
    recibe: h valor numérico y 
        g valor numérico.
    raiz cuadradada de 2hg
    devuelve: resultado de operación numérico 
    """ 
    vf=math.sqrt(2*h*g)
    return vf
def caida_velfint(g,t):
    """
    (uso de operadores, uso de funciones)
    recibe: g valor numérico y 
        t valor numérico.
    multiplica g*t
    devuelve: resultado de operación numérico 
    """ 
    vf=g*t
    return vf
def caida_tiempoh(h,g):
    """
    (uso de operadores, uso de funciones)
    recibe: h valor numérico y 
        g valor numérico.
    raiz cuadrada de (2h/g)
    devuelve: resultado de operación numérico 
    """ 
    t=math.sqrt((2*h)/(g))
    return t
def caida_tiempovf(vf,g):
    """
    (uso de operadores, uso de funciones)
    recibe: vf valor numérico y 
        g valor numérico.
    divide vf/g
    devuelve: resultado de operación numérico 
    """ 
    t=vf/g
    return t

"""
================== funciones auxiliares  =======================================
"""

def respuesta(resp):
    """
    (uso de funciones, lista, listas anidadas)
    agrega a la lista las respuestas de la formulas ocupadas, estás pueden ser otras listas.
    """
    lista.append(resp)
    
#continuar o seguir
def cont_sig(pregunta):
    """
    funcion auxiliar para imprimir
    Muestra en pantalla la lista de respuestas obtenidas
    """
    if pregunta==1:
        print("los resultados son: ",lista)
        lista.clear()

#error
def error():
    """
    funcion auxiliar para imprimir
    imprime un mensaje de error
    """
    print("Ese no es un valor valido, corra el programa de nuevo")

"""
========  parte principal del programa ========================================
"""

#crear lista
incognitas=[]
lista=[]

#Iniciar/salir Programa
ban=int(input("Introduce 1, para iniciar el programa"))
while ban==1:
    """
    (uso de ciclos)
    repite el programa hasta que el usuario escoga 
    la opcion salir y ban==0
    """
    #Menu
    ecuacion_n=int(input("¿Qué ecuación necesita?: 1. Pitagoras, 2. Regla de tres, 3.Formula general,4. Caida Libre,5. Salir"))
    #pitagoras
    if ecuacion_n==1:
        """
        (uso de condicionales y condicionales anidados)
        """
        valor=int(input("¿Qué valor quiere calcular?: 1. hipotenusa, 2. cateto"))
        #hipotenusa
        if valor==1:
            cat_1=float(input("Ingresa un cateto"))
            cat_2=float(input("Ingresa el otro cateto"))
            respues=pitagorashipo(cat_1,cat_2)
            respuesta(respues)
            preg=int(input("¿Desea ver los resultados o seguir calculando?, 1. Ver resultados 2.Seguir Calculando"))
            cont_sig(preg)
        #cateto
        elif valor==2:
            cat_1=float(input("Ingresa un cateto"))
            Hipo=float(input("Ingresa la hipotenusa"))
            if (Hipo>cat_1):
                respues=pitagorascateto(Hipo,cat_1)
                respuesta(respues)
                preg=int(input("¿Desea ver los resultados o seguir calculando?, 1. Ver resultados 2.Seguir Calculando"))
                cont_sig(preg)
            else:
                error()
        else:
            error()
        ban=1
    #regla de tres
    elif ecuacion_n==2:
        const_comp=float(input("Ingrese el valor de la constante de la cual conoce la variable"))
        vari_comp=float(input("Ingrese el valor de la variable"))
        const_inc=float(input("Ingrese el valor de la constante de la cual NO conoce la variable"))
        respues=regla_de_tres(vari_comp,const_inc,const_comp)
        respuesta(respues)
        preg=int(input("¿Desea ver los resultados o seguir calculando?, 1. Ver resultados 2.Seguir Calculando"))
        cont_sig(preg)
        ban=1
    #Formula general
    elif ecuacion_n==3:
        cuadrado=float(input("Ingrese el valor que tiene una incognita elevada al cuadrado"))
        expo=float(input("Ingrese el valor que tiene una incognita"))
        sinexpo=float(input("Ingrese el valor sin incognita"))
        fromula_gene(cuadrado,expo,sinexpo)
        respuesta(incognitas)
        preg=int(input("¿Desea ver los resultados o seguir calculando?, 1. Ver resultados 2.Seguir Calculando"))
        cont_sig(preg)
        ban=1
    #Caida libre
    elif ecuacion_n==4:
        gravedad=9.8
        valor=int(input("¿Qué valor quiere calcular?: 1. Altura, 2. Velocidad final, 3. Tiempo"))
        #altura
        if valor==1:
            tiempo=int(input("Ingrese el tiempo"))
            respues=caida_altura(tiempo,gravedad)
            respuesta(respues)
            preg=int(input("¿Desea ver los resultados o seguir calculando?, 1. Ver resultados 2.Seguir Calculando"))
            cont_sig(preg)
        #Velocidad final
        elif valor==2:
            datos=int(input("¿Qué dato quiere utilizar para encontar el valor?, 1. ALtura, 2.Tiempo"))
            if datos==1:
                altura=float(input("Ingrese la altura"))
                respues=caida_velfinh(altura,gravedad)
                respuesta(respues)
                preg=int(input("¿Desea ver los resultados o seguir calculando?, 1. Ver resultados 2.Seguir Calculando"))
                cont_sig(preg)
            elif datos==2:
                tiempo=int(input("Ingrese el tiempo"))
                respues=caida_velfint(gravedad,tiempo)
                respuesta(respues)
                preg=int(input("¿Desea ver los resultados o seguir calculando?, 1. Ver resultados 2.Seguir Calculando"))
                cont_sig(preg)
            else:
                error()
        #tiempo
        elif valor==3:
            datos=int(input("¿Qué dato quiere utilizar para encontar el valor?, 1. ALtura, 2. Velocidad final"))
            if datos==1:
                altura=float(input("Ingrese la altura"))
                respues=caida_tiempoh(altura,gravedad)
                respuesta(respues)
                preg=int(input("¿Desea ver los resultados o seguir calculando?, 1. Ver resultados 2.Seguir Calculando"))
                cont_sig(preg)
            elif datos==2:
                velfin=float(input("Ingrese la velocidad final"))
                respues=caida_tiempovf(velfin,gravedad)
                respuesta(respues)
                preg=int(input("¿Desea ver los resultados o seguir calculando?, 1. Ver resultados 2.Seguir Calculando"))
                cont_sig(preg)
            else:
                error()
        else:
            error()
        ban=1
    elif ecuacion_n==5:
        ban=0
    else:
        error()
else:
    print("hasta pronto")