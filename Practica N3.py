print ("\n")

print("--------------------")
print("* Menú de opciones *")
print("--------------------")

print("1. Conteo naturales")
print("2. Suma de 1 y N")

numero = int(input("Introduce la opción deseada:"))

if numero ==1:
    x=1
    while x<=10:
        print(x)
        x=x+1
    import time 
    time.sleep(5)


elif numero == 2:

    n=int(input("Ingrese el valor N:"))
    x=1
    a=1

    while a<=n:
        print(x)
        a=a+1
        x=x+a
    import time
    time.sleep(5)

else:
 print("La opción elegida no existe.")