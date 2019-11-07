n=int(input("Porfavor ingrese un valor entero positivo==>"))
v=0
b=0
while n<=0:
    n=int(input('Corrija el valor ingresado puesto que este no corresponde al conjunto de valores posibles====>'))

print("Aquellos valores que digan parte entera son divisiones no exactas de los números.\nSí se llega a presentar un valor que diga 'divisor' este será como dice, un divisor del número ingresado:")
for i in range(1,n+1):
    if n%i==0:
        a=("divisor {}".format(n/i))
        v +=1
    elif n%i!=0:
        a =("parte entera {}".format(n//i))
        b +=1
    #print(a) #si se quieren ver todos los divisores del numero, sacar el GATO del print
if b!=(n-2):
    print("El numero no es primo")
elif b==(n-2):
    print('El numero es primo')
    
    #dirá si el numero el primo o no.