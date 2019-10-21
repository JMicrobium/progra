N=int(input("año====>"))
b=2020
V=2020
if N%100==0:
    if N%400==0:
        print("Es un año bisiesto")
    elif N%400!=0:
        print("No es un año biesto")
elif N%100!=0:
    if N%4==0:
        print("Es un año bisiesto")
    elif N%4!=0:
        print("No es un año bisiesto")
        
    
        
        

