"""def welcome(ciudad):
    print("hola bienvenido a " + ciudad +"!")

welcome(input("dime tu ciudad: "))
"""

"""def media(info_numeros):
    suma = sum(info_numeros)
    cantidad = len(info_numeros)
    print(suma/cantidad)
    return suma/cantidad

media([1, 3, 4, 3])"""

def es_multiplo():
    if num1 % num2==0:
        print("Es Multiplo ameo")
    
    elif num2 % num1==0:
        print("Es Multiplo ameo")
        
    else:
        print("no es multiplo ameo") 
    

num1 = int(input("introduzca un numero: "))

num2 = int(input("introduzca un numero: "))

es_multiplo()