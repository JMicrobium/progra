"""The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

N=int(input("ingrese un valor====>"))
A=0
b=0
suma1=0
suma2=0
for i in range(1,N+1):
    suma1 +=(i**2) #parte 1 correcta#
    suma2 +=i
A=suma2**2-suma1
print(A)
    #resolución correcta#