# Ejemplo de uso de github 
print("Ingreso de datos")
print("--------------------")
nom=input("Ingrese su nombre: ")
while True:
    try:
        edad=int(input("Ingrese su edad: "))
        break
    except:
        
    print("Error de ingreso")
print("---------------------------")
print(f"Su numbre es {nom}")
print(f"Su edad es {edad}")
print("Programa finalizado...")
