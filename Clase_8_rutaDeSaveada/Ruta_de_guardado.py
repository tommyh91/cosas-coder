ruta = "C:/Users/m.hinchliff.mathew/Desktop/Coderhouse"

"""miArchivo = open(ruta+"/Archivo1.txt", "w")

miArchivo.write("Hola Mundo")

miArchivo.close()"""

f = open(ruta+"/HobbyDelPibe.txt", "w")

for x in range(3):

    Hobby = input("ingrese su hobby favorito: ")

    f.write(Hobby+", ")

f.close()