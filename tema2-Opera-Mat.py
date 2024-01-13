num1=20
num2=4

print("La suma es: ", (num1+num2))
print("La resta es: ", (num1-num2))
print("La multiplicación es: ", (num1*num2))
print("La división exacta es: ", (num1//num2))
print("La división es: ", (num1/num2))
print("La potencia es: ", (num1 ** num2))

#Concatenacion

texto="hola"
texto2="Mundo"
textoFinal=texto + " " + texto2

print(textoFinal)
print("El saludo es: %s %s" %(texto,texto2))
saludoFinal="Saludo {} {}".format(texto, texto2)
print(saludoFinal)

saludoFinal2="Saludo 2: {y} {x}".format(y=texto,x=texto2)
print(saludoFinal2)