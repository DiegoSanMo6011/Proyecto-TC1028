"""
Proyecto TC1028 "Mates Utiles y bonitas :)"
Calculadora de: Formula general, Regla de tres, Teorema de Pitagoras
"""
#bibliotecas
import math
#Menu
ecuacion_n=int(input("¿Qué ecuación necesita?: 1. Pitagoras, 2. Regla de tres, 3.Formula general"))
#Teorema de Pitagoras
if ecuacion_n==1:
    valor=int(input("¿Qué valor quiere calcular?: 1. hipotenusa, 2. cateto"))
    if valor==1:
        cateto_1=float(input("Ingresa un cateto"))
        cateto_2=float(input("Ingresa el otro cateto"))
        Hipo= math.sqrt(cateto_1**2+cateto_2**2)
        print("La hipotenusa es:",Hipo)
    elif valor==2:
        cateto_1=float(input("Ingresa un cateto"))
        Hipo=float(input("Ingresa la hipotenusa"))
        cateto_2=math.sqrt(Hipo**2-cateto_1**2)
        print("El cateto que busas es:",cateto_2)
    else:
        print ("Ese valor no es valido, vuelve a correr el programa")
#Regla de tres
elif ecuacion_n==2:
    constante_comp=float(input("Ingrese el valor de la constante de la cual conoce la variable"))
    variable_comp=float(input("Ingrese el valor de la variable"))
    constante_inc=float(input("ngrese el valor de la constante de la cual NO conoce la variable"))
    resp=(variable_comp*constante_inc)/constante_comp
    print("La respuesta es:",resp)
#Formula general de una ecuacion cuadratica
elif ecuacion_n==3:
    a=float(input("Ingrese el valor que tiene una incognita elevada al cuadrado"))
    b=float(input("Ingrese el valor que tiene una incognita"))
    c=float(input("Ingrese el valor sin incognita"))
    if a!= 0:
        incognita_1=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
        incognita_2=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)
        print("las incognitas son:",incognita_1," y ",incognita_2)
    else:
        print("El valor de a no puede ser 0")
#En caso de que el usuario ingrese un numero erroneo
else:
     print ("Ese valor no es valido, vuelve a correr el programa")