sw=1
entrada_n=5500
entrada_j=7000
entrada_a=9000
cant_total_n=0
cant_total_j=0
cant_total_a=0
cant_n=0
cant_j=0
cant_a=0
venta_n=0
venta_j=0
venta_a=0
venta_total=0
venta_total_dia=0

while sw==1:
    print("_________________________________")
    print("Bienvenido a CineMoro")
    print("Tenemos las siguientes opciones: ")
    print("1. Niño con un valor de $5.500\n (edad entre 1-13)")
    print("2. Joven con un valor de $7.0000\n (edad entre 14-21)")
    print("3. Adulto con un valor de $9.0000\n (edad de 22 en adelante)")
    print("4. Boleta")
    print("5. Terminar jornada")
    print("Porfavor elija una opcion")
    try:
        op=int(input("Ingrese una opcion: "))
        if op==1:
            cant_n=int(input("Ingrese la cantidad que desea: "))
            cant_total_n=cant_total_n+cant_n
            venta_n=venta_n+(cant_n*entrada_n)
        elif op==2:
            cant_j=int(input("Ingrese la cantidad que desea"))
            cant_total_j=cant_total_j+cant_j
            venta_j=venta_j+(cant_j*entrada_j)
        elif op==3:
            cant_a=int(input("Ingrese la cantidad que desea"))
            cant_total_a=cant_total_a+cant_a
            venta_a=venta_a+(cant_a*entrada_a)
        elif op==4:
            venta_total=venta_a+venta_j+venta_n
            venta_total_dia=venta_total_dia+venta_total
            print("--------------------------------------------------")
            print("Muchas gracias por su compra")
            print("Su total es de: ")
            print(f"Niños:     Total entradas:{cant_n} Total {venta_n}")
            print(f"Joven:     Total entradas:{cant_j} Total {venta_j}")
            print(f"Adulto:    Total entradas:{cant_a} Total {venta_a}")
            print("--------------------------------------------------")
            print(f"                          Subtotal: {venta_total}")
            venta_n=0
            venta_j=0
            venta_a=0
            cant_n=0
            cant_j=0
            cant_a=0   
            venta_total=0         
        elif op==5:
            entradas_n_por=int(cant_total_n/cant_total)*100
            entradas_j_por=int(cant_total_j/cant_total)*100
            entradas_a_por=int(cant_total_a/cant_total)*100
            cant_total=cant_total_a+cant_total_j+cant_total_n
            print("Terminando...")
            print(f"Su total de ventas es {venta_total_dia}")
            print(f"Su total de entradas fue {cant_total}")
            print(f"Entradas niño: {entradas_n_por}%")
            print(f"Entradas joven: {entradas_j_por}%")
            print(f"Entradas adulto: {entradas_a_por}%")
        else:
            print("Opcion no valida")
    except:
        print("Error opcion ingresada no valida")

