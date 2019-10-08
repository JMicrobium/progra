A=float(input("Ingrese un numero======>"))
B=float(input("Ingrese un numero======>"))
C=float(input("Ingrese un numero======>"))
if A>B and A>C:
    if B>C:
        print("Descendente",A,B,C)
    elif B<C:
        print("Descendente",A,C,B)
elif B>A and B>C:
    if A>C:
        print("Descendente",B,A,C)
    elif A<C:
        print("Descendente",B,C,A)
elif C>A and C>B:
    if A>B:
        print("Descendente",C,A,B)
    elif A<B:
        print("Descendente",C,B,A)
        
        