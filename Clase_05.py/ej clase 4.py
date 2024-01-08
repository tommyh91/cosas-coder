"""for numero in range(1,21 ):
    print(numero)
    """

"""conjunto7 = {9,23, "hola", "mesa", 13,10.3}"""

"""while len(conjunto7)>0:
    eliminado = conjunto7.pop()
    print("se ha eliminado el elemento: ", eliminado)
    print("El conjunto queda de la siguiente manera: ", conjunto7)"""

"""for x in conjunto7:
    if type(x)==str:
        print("cadena: ",x)
    elif type(x)== float:
        print("decimal: ",x)"""

dic_monedas = {"Dolar":"$", "Euro":"E", "Libra":"L"}

moneda = input("Elija la divisa qe desea visualizar: ")

print(dic_monedas.get(moneda, "no esta capo"))

