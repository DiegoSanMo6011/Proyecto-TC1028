"""
Proyecto TC1028 "Mates Utiles y bonitas :)"
Calculadora de: Formula general, Regla de tres, Teorema de Pitagoras
"""
#bibliotecas
import math
#funciones pitagoras
def pitagorascateto(hipo,cateto_1):
    cateto_2=math.sqrt(hipo**2-cateto_1**2)
    return cateto_2
def pitagorashipo(cateto_1,cateto_2):
    hipo= math.sqrt(cateto_1**2+cateto_2**2)
    return hipo
#funcion regla de tres
def regla_de_tres(variable_comp,constante_inc,constante_comp):
     resp=(variable_comp*constante_inc)/constante_comp
     return resp
#funcion regla general
def fromula_gene(a,b,c):
    if a!= 0:
        incognita_1=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
        incognita_2=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)
        return incognita_1,incognita_2
    else:
        return "El valor de a no puede ser 0"
def caida_altura(t,g):
    
    h=1/2*g*t**2
    return h
def caida_velfinh(h,g):
    vf=math.sqrt(2*h*g)
    return vf
def caida_velfint(g,t):
    vf=g*t
    return vf
def caida_tiempoh(h,g):
    t=math.sqrt((2*h)/(g))
    return t
def caida_tiempovf(vf,g):
    t=vf/g
    return t
#respuesta
def respuesta(resp):
    lista.append(resp)
    
#continuar o seguir
def cont_sig(pregunta):
    if pregunta==1:
        print("los resultados son: ",lista)
        lista.clear()
#error
def error():
    print("Ese no es un valor valido, corra el programa de nuevo")
#crear lista
lista=[]
#Iniciar/salir Programa
ban=int(input("Introduce 1, para iniciar el programa"))
while ban==1:
    #Menu
    ecuacion_n=int(input("¿Qué ecuación necesita?: 1. Pitagoras, 2. Regla de tres, 3.Formula general,4. Caida Libre,5. Salir"))
    #pitagoras
    if ecuacion_n==1:
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
        respues=fromula_gene(cuadrado,expo,sinexpo)
        respuesta(respues)
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


