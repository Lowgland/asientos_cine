def crear_matriz(filas, columnas):
    matriz=[]
    for f in range(filas):
        fila=[]
        for c in range(columnas):
            fila.append("L")
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{elem:5}" for elem in fila))

def reservar_asiento(matriz, fila, columna):
    if fila<0 or fila>=len(matriz) or columna<0 or columna>=len(matriz[0]):
        print("No hay un asiento en esa posicion")
        return False
    elif matriz[fila][columna]=="X":
        print("El asiento ya esta ocupado")
        return False
    matriz[fila][columna]="X"
    print("Asiento reservado con exito")
    return True

def liberar_asientos(matriz, fila, columna):
    if fila<0 or fila>=len(matriz) or columna<0 or columna>=len(matriz[0]):
        print("No hay un asiento en esa posicion")
        return False
    if matriz[fila][columna]=="L":
        print("Ese asiento ya está libre")
        return False
    matriz[fila][columna]="L"
    print("Asiento liberado correctamente")
    return True

def contar_asientos_libres_ocupados(matriz):
    libre=0
    ocupado=0
    for fila in matriz:
        for asiento in fila:
            if asiento=="L":
                libre=libre+1
            else:
                ocupado=ocupado+1
    return libre, ocupado

filas=int(input("Ingrese el numero de filas del cine: "))
columnas=int(input("Ingrese el numero de columnas del cine: "))
matriz=crear_matriz(filas, columnas)

while True:
    print("\n ===MENU===")
    print("1. Mostrar sala")
    print("2. reservar asiento")
    print("3. liberar asiento")
    print("4. Contar asientos libres y ocupados")
    print("5. Salir")
    opcion=int(input("Ingrese una opcion (del 1 al 5): "))
    
    if opcion==1:
        imprimir_matriz(matriz)
    elif opcion==2:
        fila=int(input("Ingrese la fila del asiento a reservar: "))-1
        columna=int(input("Ingrese la columna del asiento a reservar: "))-1
        reservar_asiento(matriz, fila, columna)
    elif opcion==3:
        fila=int(input("Ingrese la fila del asiento a liberar: "))-1
        columna=int(input("Ingrese la columna del asiento a liberar: "))-1
        liberar_asientos(matriz, fila, columna)
    elif opcion==4:
        libres, ocupados=contar_asientos_libres_ocupados(matriz)
        print(f"Asientos libres: {libres} // Asientos ocupados: {ocupados}")
    elif opcion==5:
        print("Saliendo del programa...")
        print("Espero que vuelvas pronto! :D")
        break
    else:
        print("Opcion invalida, ingresa un numero del 1 al 5")