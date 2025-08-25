#TP UNIDAD ESTRUCTURAS SECUENCIALES
#ejercicio 1
print ("Hola Mundo!")

#ejercicio 2
nombre=input("¿Como te llamas?")
print(f"Hola {nombre}!")

#ejercicio 3
nombre=input("¿Como te llamas?")
apellido=input("¿Como es tu apellido?")
pais=input("¿Donde vives?")
edad=int(input("¿Que edad tenes?"))
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}. ")

#ejercicio 4
radio=float(input("Ingrese el área del circulo."))
area= 3.14 * (radio**2)
perimetro= 2 * 3.14 * radio

print("Al área del circulo es : ", area)
print("Al perimetro del circulo es : ", perimetro)

#ejercicio 5
segundos=input("Ingrese segundos.")
horas= segundos // 60
print(f"la cantidad de horas que equivale {segundos} seg es {horas}horas")

#ejercicio 6
numero=float(input("Ingrese un numero"))
print("La tabla de multiplicar de dicho numero es: ")
print(numero * 1 )
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)

#ejercicio 7
num1= float(input("Ingrese primer numero distinto a cero."))
num2= float(input("Ingrese segundo numero distinto a cero."))

print("Resultado de sumar, restar, multiplicar y dividir estos dos numeros:")
print("suma : ",num1 + num2)
print("resta : ",num1 - num2)
print("multiplicacion : ",num1 * num2)
print("division : ",num1 / num2)

#ejercicio 8 
altura=float(input("Ingrese su altura en metros."))
peso=float(input("Ingrese su peso en kilos."))

masacorporal= peso / (altura)**2
print("El indice de masa corporal es:",masacorporal)

#ejercicio 9 
celcius=float(input("Ingrese temperatura en grado celcius."))
fahrenheit= 9/5 * celcius + 32
print(f"La temperatura equivalente de {celcius} grados celcius a fahrenheit es {fahrenheit} grados fahrenheit.")

#ejercicio 10
num1= float(input("Ingrese primer numero")) 
num2= float(input("Ingrese segundo numero"))
num3= float(input("Ingrese tercer numero")) 
promedio= (num1+num2+num3)/3
print("El promedio de estos tres numeros es de: ", promedio )