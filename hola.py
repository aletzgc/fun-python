#E1 intercambio de dos valores
print("Ejercicio 1: intercambio de valores")
val1 = input(" A -> ")
val2 = input(" B -> ")
val1, val2 = val2, val1
print("El resultado del Usuario_1 será:" ,val1)
print("El resultado del Usuario_2 será:" ,val2)
print("\n")

#E2 operaciones aritmeticas
print("Ejercicio 2 operaciones aritmeticas")

num1 =float(input("Introduzca el valor del numero1: "))
num2 =float(input("Introduzca el valor del numero1: "))

print("La suma final es: "    ,num1+num2)
print("La resta final es: "   ,num1-num2)
print("El residuo final es: " ,num1%num2)
print("\n")

#E3
lado1 = float(input("Introduzca lado 1: ")) 
lado2 = float(input("Introduzca lado 2: "))
lado3 = float(input("Introduzca lado 3: "))
if(lado1==lado2 and lado2==lado3):
    print ("Triangulo Equilatero")
    print("")
elif(lado1==lado2 or lado1==lado3 or lado2==lado3):
    print ("Triangulo Isoceles")
    print("")
elif (lado1!=lado2 or lado1!=lado3 or lado2!=lado3):
    print ("Triangulo Escaleno \n")

#E4
lista1 = [1, 2, 3, -4, 5, 6, 7, 8, -9, 10, -11, 12, -13, -14, 15]
num_pos, num_neg = 0, 0
num = 0
  
while(num < len(lista1)):
    if lista1[num] >= 0: 
        num_pos += 1
    else: 
        num_neg += 1
    num += 1
print("Lista de valores numericos: \n" ,lista1)
print("Lista de numeros positivos: ", num_pos) 
print("Lista de numeros negativos: ", num_neg)