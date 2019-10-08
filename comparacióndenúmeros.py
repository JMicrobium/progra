A=float(input("Ingrese un numero======>"))
B=float(input("Ingrese un numero======>"))
C=float(input("Ingrese un numero======>"))
if A>B and A>C:
    if B>C:
        print(A,B,C)
    elif B<C:
        print(A,C,B)
elif B>A and B>C:
    if A>C:
        print(B,A,C)
    elif A<C:
        print(B,C,A)
elif C>A and C>B:
    if A>B:
        print(C,A,B)
    elif A<B:
        print(C,B,A)
        
        