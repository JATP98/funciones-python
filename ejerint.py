#Escribir una función que cuente la cantidad de apariciones de
# cada carácter en una cadena de texto, y los devuelva en un diccionario.
def cuentaCaracteres(cadena):
	diccionario={}
	for caracter in cadena:
		if caracter in diccionario.keys():
			diccionario[caracter]=diccionario[caracter]+1
		else:
			diccionario[caracter]=1
	return diccionario

caracter=str(input("Escribe una frase: "))
#caractercontar=input("Dime un caracter: ")
contador=0
#for x in caracter:
#	if x == caractercontar:
#		contador=contador+1
print(cuentaCaracteres(caracter))
