A=float(input("Ingrese un numero======>"))
B=float(input("Ingrese un numero======>"))
C=float(input("Ingrese un numero======>"))
if A>B and A>C:
    if B>C:
        print("Ascendente",C,B,A)
    elif B<C:
        print("Ascendente",B,C,A)
elif B>A and B>C:
    if A>C:
        print("Ascendente",C,A,B)
    elif A<C:
        print("Ascendente",A,C,B)
elif C>A and C>B:
    if A>B:
        print("Ascendente",B,A,C)
    elif A<B:
        print("Ascendente",A,B,C)
        