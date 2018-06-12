# Ejercicios funciones
euros = ()
lista=[]
horas=()
n_comiunicacines=int(input ("Cuantas comunicaciones has tenido: "))
tarifa = int (input("Dime una tarifa: "))

def pasar_a_segundos (horas,minutos,segundos):
	return horas*3600+minutos*60+segundos
def calcular_coste (tarifa,segundos):
	return segundos*tarifa
def convertir_a_euros (centimos):
	return round(centimos/100,2)

for x in range (n_comiunicacines):
	horas = int(input("Dime numero de horas: "))
	minutos = int(input("Dime numero de mintos: "))
	segundos = int(input("Dime numero de segundos: "))
	segs = pasar_a_segundos(horas,minutos,segundos)
	coste = calcular_coste(tarifa,segs)
	euros=convertir_a_euros(coste)
	lista.append(euros)

print ("Cada llamada te ha costado: ", lista, "€")
print ("El total es: ", sum(lista), "€")
