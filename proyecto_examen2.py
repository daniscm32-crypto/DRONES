drones = []
misiones = []
grafo = {}
cola_misiones = []
raiz = None

def registrar_dron():
    codigo = input("Código: ")
    modelo = input("Modelo: ")
    if modelo == "":
        print("El modelo no puede estar vacío")
        return
    try:
        velocidad = int(input("Velocidad: "))
        if velocidad <= 0:
            print("La velocidad debe ser un número mayor a cero")
            return
    except ValueError:
        print("Ingrese una cantidad correcta")
        return
    try:
        capacidad = int(input("Capacidad: "))
        if capacidad <= 0:
            print("La capacidad debe ser un número mayor a cero")
            return
    except ValueError:
        print("Ingrese una cantidad correcta")
        return
    try:
        bateria = int(input("Batería: "))
        if bateria < 0 or bateria > 100:
            print("La batería debe estar entre 0 y 100")
            return
    except ValueError:
        print("Ingrese una cantidad correcta")
        return

    dron = {
        "codigo": codigo,
        "modelo": modelo,
        "velocidad": velocidad,
        "capacidad": capacidad,
        "bateria": bateria,
        "estado": "Disponible"
    }
    drones.append(dron)
    print("Dron registrado.")


def mostrar_drones():
    if not drones:
        print("No hay drones registrados.")
        return
    for d in drones:
        print(f"{d['codigo']} | {d['modelo']} | Vel: {d['velocidad']} | Cap: {d['capacidad']} | Bat: {d['bateria']}% | {d['estado']}")


def eliminar_dron():
    codigo = input("Código del dron a eliminar: ")
    for i in range(len(drones)):
        if drones[i]["codigo"] == codigo:
            drones.pop(i)
            print("Dron eliminado.")
            return
    print("Dron no encontrado.")


def registrar_mision():
    global raiz
    codigo = input("Código: ")
    zona = input("Zona: ")
    tipo = input("Tipo de emergencia: ")
    try:
        prioridad = int(input("Prioridad (1-5): "))
        personas = int(input("Personas afectadas: "))
        distancia = int(input("Distancia: "))
    except ValueError:
        print("Ingrese valores numéricos correctos.")
        return None

    mision = {
        "codigo": codigo,
        "zona": zona,
        "tipo": tipo,
        "prioridad": prioridad,
        "personas": personas,
        "distancia": distancia,
        "estado": "Pendiente"
    }
    misiones.append(mision)
    raiz = insertar_bst(raiz, mision)
    cola_misiones.append(mision)
    print("Misión registrada.")
    return mision


def mostrar_misiones():
    if not misiones:
        print("No hay misiones registradas.")
        return
    for m in misiones:
        print(f"{m['codigo']} | {m['zona']} | {m['tipo']} | Prioridad: {m['prioridad']} | {m['estado']}")


def eliminar_mision():
    codigo = input("Código de la misión a eliminar: ")
    for i in range(len(misiones)):
        if misiones[i]["codigo"] == codigo:
            misiones.pop(i)
            print("Misión eliminada.")
            return
    print("Misión no encontrada.")

def menu_drones():
    while True:
        print("\n--- DRONES ---")
        print("1. Registrar dron")
        print("2. Mostrar drones")
        print("3. Eliminar dron")
        print("4. Regresar al menú principal")
        opcion = input("Ingrese una opción válida: ")
        match opcion:
            case "1":
                registrar_dron()
            case "2":
                mostrar_drones()
            case "3":
                eliminar_dron()
            case "4":
                return
            case _:
                print("Opción inválida.")


def menu_misiones():
    while True:
        print("\n--- MISIONES ---")
        print("1. Registrar misión")
        print("2. Mostrar misiones")
        print("3. Eliminar misión")
        print("4. Regresar al menú principal")
        opcion = input("Ingrese una opción válida: ")
        match opcion:
            case "1":
                registrar_mision()
            case "2":
                mostrar_misiones()
            case "3":
                eliminar_mision()
            case "4":
                return
            case _:
                print("Opción inválida.")


def menu_principal():
    while True:

        print(" POLIRESCUE TECHNOLOGIES ")

        print("1. Registrar información de drones")
        print("2. Registrar información de misiones")
        print("3. Gestión de zonas y rutas")
        print("4. Cola de misiones")
        print("5. Árbol BST de misiones")
        print("6. Organización de misiones")
        print("7. Búsqueda lineal (dron / misión)")
        print("8. Búsqueda binaria de dron")
        print("9. Verificar camino entre zonas (BFS)")
        print("10. Calcular ruta mínima (Dijkstra)")
        print("11. Simulación completa de rescate")
        print("0. Salir")

        opcion = input("\nSeleccione: ")

        match opcion:
            case "1":
                menu_drones()
            case "2":
                menu_misiones()
            case "3":
                #menu_zonas()
            case "4":
                #menu_cola()
            case "5":
                #menu_bst()
            case "6":
                print("1. Buscar dron")
                print("2. Buscar misión")
                sub = input("Seleccione: ")
                if sub == "1":
                 #   busqueda_lineal_dron()
                elif sub == "2":
                  #  busqueda_lineal_mision()
                else:
                    print("Opción inválida.")
            case "7":
                #busqueda_binaria_dron()
            case "8":
                origen = input("Zona origen: ")
                destino = input("Zona destino: ")
                #bfs_existe_camino(origen, destino)
            case "9":
                origen = input("Zona origen: ")
                destino = input("Zona destino: ")
                #dijkstra(origen, destino)
            case "10":
                #simulacion_rescate()
            case "0":
                print("Saliendo del sistema.....")
                break
            case _:
                #print("Opción inválida.")


menu_principal()  


