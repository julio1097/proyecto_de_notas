notas = []
continuar = "si"
while continuar == "si":
	nota = str(input("Ingrese su nota: "))
	notas.append(nota)
	continuar= str(input("¿Desea continuar?: "))

texto =("\n").join(notas)
f = open("notasguardadas.txt", "w")
f.write(texto)
f.close()