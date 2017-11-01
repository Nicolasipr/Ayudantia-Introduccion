import random
import sys
import os

def polinomio1(x):
    y=(x*4 + x*3 + 2*2 -x)
    return y

def polinomio2(x):
    y=(4*x + 3*x + 1/2*2 -x)
    return y

def FahrenheitCelcius(F):
    C=(F-32)*5/9
    return C

def PiesPulAMetros(Pie, Pul):
    MetroPies=Pie*12*2.54/100
    MetroPulgadas=2.54*Pul/100
    print("\nEl equivalente de", Pie, " pies es" , MetroPies," metros \nEl equivalente de ", Pul," pulgadas es ", MetroPulgadas," metros")
    
def JarroVasos(N, X):
    cc=N*1000/X
    return cc


while True:
    
    print('\n\t\t Ejercicios Propuestos\n\n'
          '1. Funciones Escritas\n'
          '\ta. Evaluar Polinomio 4x + 3x + 2*2 - x\n'
          '\tb. Evaluar Polinomio 4x + 3x + 1/2*2 -x\n'
          '2. Problemas Resueltos\n'
          '\ta. Convesor grados Fahrenheit a Celsius\n'
          '\tb. Longitud de pies y pulgadas expresada en metros\n'
          '\tc. Llenar un Jarro de N litros con vasos de X cc\n')

    eleccion=input("Ingrese su opcion en formato numeroletra : ")

    if(eleccion=="1a"):
        x=int(input("\nIngrese el numero a evaluar: "))
        print(polinomio1(x))
        input("Ingrese una tecla para continuar...")
        os.system('cls')                           #os.system('clear') en Linux/OSx#
        
    elif(eleccion=="1b"):
        x=int(input("\nIngrese el numero a evaluar: "))
        print(polinomio2(x))
        input("Ingrese una tecla para continuar...")
        os.system('cls')
        
    elif(eleccion=="2a"):
        F=float(input("\nIngrese La temperatura en Fahrenheit que desea convertir: "))
        print(FahrenheitCelcius(F))
        input("Ingrese una tecla para continuar...")
        os.system('cls')
        
    elif(eleccion=="2b"):
        Pie=float(input("\nIngrese  La cantidad de pies que dese transformar: "))
        Pul=float(input("Ahora ingrese la cantidad de pulgadas: "))
        print(PiesPulAMetros(Pie, Pul))
        input("Ingrese una tecla para continuar...")
        os.system('cls')
        
    elif(eleccion=="2c"):
        N= float(input("\nIngrese  La cantidad de Litros en su jarro: "))
        X= float(input("Ahora ingrese la cantidad de cc de sus vasos: "))
        print(JarroVasos(N, X))
        input("Ingrese una tecla para continuar...")
        os.system('cls')
        
    else:
        print('\n\nFormato no valido'
              '\nSi desea el ejercicio  1.- a. ingrese \"1a\"')
        
                                    

        

    
