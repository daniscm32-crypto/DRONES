drones = []
misiones = []
grafo = {}
cola_misiones = []
raiz = None

class Nodo:
    def __init__(self, mision):
        self.mision = mision
        self.codigo = mision["codigo"]
        self.izquierda = None
        self.derecha = None


def registrar_dron():
    codigo = input("Código: ")
    for d in drones:
        if d["codigo"] == codigo:
            print("Error: El código ya está registrado.")
            return
    modelo = input("Modelo: ")
    if modelo == "":
        print("El modelo no puede estar vacío")
        return
    try:
        velocidad = int(input("Velocidad (km/h): "))
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
    for d in drones:
        if d["codigo"] == codigo:
            print("Error: El código ya está registrado.")
            return
    zona = input("Zona: ")
    if zona not in grafo:
        grafo[zona] = []
        print(f"Zona '{zona}' nueva, registrada automáticamente.")
    tipo = input("Tipo de emergencia: ")
    try:
        prioridad = int(input("Prioridad (1-5): "))
        if prioridad < 1 or prioridad > 5:
            print("La prioridad debe estar entre 1 y 5")
            return None
        personas = int(input("Personas afectadas: "))
        if personas < 0:
            print("Las personas afectadas no pueden ser negativas")
            return None
        distancia = int(input("Distancia (km): "))
        if distancia < 0:
            print("La distancia no puede ser negativa")
            return None
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
    raiz = insertar_bst(raiz, mision)   # también queda registrada en el árbol
    cola_misiones.append(mision)        # y entra a la cola de pendientes
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


def registrar_zona():
    """Agrega una zona nueva al grafo (nodo sin conexiones todavía)."""
    zona = input("Nombre de la zona: ")
    if zona in grafo:
        print("La zona ya existe.")
        return
    grafo[zona] = []
    print("Zona registrada.")


def registrar_ruta():
    """Crea una ruta (arista) entre dos zonas ya registradas, con su
    distancia en km. El grafo no es dirigido, así que la conexión se
    guarda en ambos sentidos."""
    origen = input("Zona origen: ")
    destino = input("Zona destino: ")
    if origen not in grafo or destino not in grafo:
        print("Ambas zonas deben estar registradas.")
        return
    try:
        distancia = int(input("Distancia (km): "))
        if distancia <= 0:
            print("La distancia debe ser mayor a cero")
            return
    except ValueError:
        print("Ingrese un valor numérico.")
        return
    grafo[origen].append((destino, distancia))
    grafo[destino].append((origen, distancia))
    print("Ruta registrada.")


def mostrar_grafo():
    if not grafo:
        print("No hay zonas registradas.")
        return
    for zona in grafo:
        conexiones = ", ".join([f"{v}({d}km)" for v, d in grafo[zona]])
        print(f"{zona} -> {conexiones}")


def atender_mision():
    if not cola_misiones:
        print("No hay misiones pendientes.")
        return None
    mision = cola_misiones.pop(0)
    mision["estado"] = "Atendida"
    print(f"Misión {mision['codigo']} atendida.")
    return mision


def mostrar_siguiente_mision():
    if not cola_misiones:
        print("No hay misiones en cola.")
        return
    print(f"Siguiente misión: {cola_misiones[0]['codigo']} - Zona: {cola_misiones[0]['zona']}")


def busqueda_lineal_dron():
    if not drones:
        print("No hay drones registrados.")
        return None
        
    codigo = input("Código del dron a buscar: ")
    comparaciones = 0
    
    for d in drones:
        comparaciones += 1
        print(f"Comparando con el dron: {d['codigo']}")
        
        if d["codigo"] == codigo:
            print(f"\n¡Dron Encontrado! (Comparaciones realizadas: {comparaciones})")
            print("-" * 50)
            print(f"Código:    {d['codigo']}")
            print(f"Modelo:    {d['modelo']}")
            print(f"Velocidad: {d['velocidad']} km/h")
            print(f"Capacidad: {d['capacidad']}")
            print(f"Batería:   {d['bateria']}%")
            print(f"Estado:    {d['estado']}")
            print("-" * 50)
            return d
            
    print(f"Dron no encontrado. Comparaciones realizadas: {comparaciones}")
    return None

def busqueda_lineal_mision():
    if not misiones:
        print("No hay misiones registradas.")
        return None
        
    codigo = input("Código de la misión a buscar: ")
    comparaciones = 0
    
    for m in misiones:
        comparaciones += 1
        print(f"Comparando con la misión: {m['codigo']}")
        
        if m["codigo"] == codigo:
            print(f"\n¡Misión Encontrada! (Comparaciones realizadas: {comparaciones})")
            print("-" * 50)
            print(f"Código:    {m['codigo']}")
            print(f"Zona:      {m['zona']}")
            print(f"Tipo:      {m['tipo']}")
            print(f"Prioridad: {m['prioridad']}")
            print(f"Estado:    {m['estado']}")
            print("-" * 50)
            return m
            
    print(f"Misión no encontrada. Comparaciones realizadas: {comparaciones}")
    return None

def ordenar_por_codigo(lista):

    copia = lista.copy()
    for i in range(1, len(copia)):
        actual = copia[i]
        j = i - 1
        while j >= 0 and copia[j]["codigo"] > actual["codigo"]:
            copia[j + 1] = copia[j]
            j -= 1
        copia[j + 1] = actual
    return copia


def busqueda_binaria_dron():
    if not drones:
        print("No hay drones registrados.")
        return None
    codigo_buscado = input("Código del dron a buscar: ")
    lista_ordenada = ordenar_por_codigo(drones)
    inicio = 0
    fin = len(lista_ordenada) - 1
    while inicio <= fin:
        mitad = (inicio + fin) // 2
        dron_del_medio = lista_ordenada[mitad]
        print(f"Buscando entre posiciones [{inicio} y {fin}]. Probando con el código del medio: {dron_del_medio['codigo']}")

        if dron_del_medio["codigo"] == codigo_buscado:
            print(f"Dron encontrado en la posición {mitad}")
            return dron_del_medio
        elif dron_del_medio["codigo"] < codigo_buscado:
            inicio = mitad + 1
            print("El código buscado es mayor. Descartamos la mitad izquierda.")
        else:
            fin = mitad - 1
            print("El código buscado es menor. Descartamos la mitad derecha.")

    print("Dron no encontrado en el sistema.")
    return None


def burbuja_prioridad():
    lista = misiones
    if not lista:
        print("No hay misiones registradas.")
        return
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            print(f"Comparando: {lista[j]['codigo']} (P{lista[j]['prioridad']}) vs {lista[j + 1]['codigo']} (P{lista[j + 1]['prioridad']})")
            if lista[j]["prioridad"] < lista[j + 1]["prioridad"]:
                print(f"Intercambiando: {lista[j]['codigo']} <-> {lista[j + 1]['codigo']}")
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        print("Lista actual:", [m["codigo"] for m in lista])
    print("Misiones ordenadas por prioridad.")


def insercion_bateria():
    lista = drones
    if not lista:
        print("No hay drones registrados.")
        return
    for i in range(1, len(lista)):
        actual = lista[i]
        print(f"Insertando: {actual['codigo']} (Bat: {actual['bateria']}%)")
        j = i - 1
        while j >= 0 and lista[j]["bateria"] > actual["bateria"]:
            print(f"Moviendo: {lista[j]['codigo']}")
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
        print("Lista actual:", [d["codigo"] for d in lista])
    print("Drones ordenados por batería.")


def mergesort(lista):

    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    print(f"Dividiendo: {[d['codigo'] for d in lista]} -> {[d['codigo'] for d in izquierda]} | {[d['codigo'] for d in derecha]}")
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]["velocidad"] <= derecha[j]["velocidad"]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    print(f"Mezclando: {[d['codigo'] for d in resultado]}")
    return resultado


def mergesort_velocidad():
    if not drones:
        print("No hay drones registrados.")
        return
    ordenado = mergesort(drones)
    drones[:] = ordenado
    print("Resultado parcial:", [d["codigo"] for d in drones])
    print("Drones ordenados por velocidad.")


def particion(lista, low, high):
    pivote = lista[high]["distancia"]
    print(f"Pivote: {lista[high]['codigo']} (Distancia: {pivote})")
    i = low - 1
    for j in range(low, high):
        if lista[j]["distancia"] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[high] = lista[high], lista[i + 1]
    print(f"Partición: {[m['codigo'] for m in lista[low:high + 1]]}")
    return i + 1


def quicksort_helper(lista, low, high):
    if low < high:
        pivote_pos = particion(lista, low, high)
        quicksort_helper(lista, low, pivote_pos - 1)
        quicksort_helper(lista, pivote_pos + 1, high)

def quicksort_distancia():
    if not misiones:
        print("No hay misiones registradas.")
        return
    quicksort_helper(misiones, 0, len(misiones) - 1)
    print("Resultado:", [m["codigo"] for m in misiones])
    print("Misiones ordenadas por distancia.")

def insertar_bst(nodo, mision):
    if nodo is None:
        return Nodo(mision)
    if mision["codigo"] < nodo.codigo:
        nodo.izquierda = insertar_bst(nodo.izquierda, mision)
    elif mision["codigo"] > nodo.codigo:
        nodo.derecha = insertar_bst(nodo.derecha, mision)
    return nodo


def buscar_bst(nodo, codigo):
    if nodo is None:
        print("No encontrado.")
        return None
    print(f"Visitando nodo: {nodo.codigo}")
    if codigo == nodo.codigo:
        print("Encontrado")
        return nodo.mision
    elif codigo < nodo.codigo:
        return buscar_bst(nodo.izquierda, codigo)
    else:
        return buscar_bst(nodo.derecha, codigo)


def preorden(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo:
        resultado.append(nodo.codigo)
        preorden(nodo.izquierda, resultado)
        preorden(nodo.derecha, resultado)
    return resultado

def inorden(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo:
        inorden(nodo.izquierda, resultado)
        resultado.append(nodo.codigo)
        inorden(nodo.derecha, resultado)
    return resultado


def postorden(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo:
        postorden(nodo.izquierda, resultado)
        postorden(nodo.derecha, resultado)
        resultado.append(nodo.codigo)
    return resultado


def menu_bst():
    global raiz
    while True:
        print("\n--- BST DE MISIONES ---")
        print("1. Buscar misión por código")
        print("2. Recorrido Preorden")
        print("3. Recorrido Inorden")
        print("4. Recorrido Postorden")
        print("5. Volver")
        opcion = input("Seleccione: ")
        match opcion:
            case "1":
                codigo = input("Código a buscar: ")
                buscar_bst(raiz, codigo)
            case "2":
                print("Preorden:", preorden(raiz))
            case "3":
                print("Inorden:", inorden(raiz))
            case "4":
                print("Postorden:", postorden(raiz))
            case "5":
                return
            case _:
                print("Opción inválida.")


def bfs_existe_camino(origen, destino):
    if origen not in grafo or destino not in grafo:
        print("Zona no encontrada en el grafo.")
        return False
    visitados = []
    cola_bfs = [origen]
    while cola_bfs:
        actual = cola_bfs.pop(0)
        if actual not in visitados:
            print(f"Visitando: {actual}")
            visitados.append(actual)
            print(f"Cola actual: {cola_bfs}")
            print(f"Nodos visitados: {visitados}")
            if actual == destino:
                print("Camino encontrado.")
                return True
            for vecino, distancia in grafo[actual]:
                if vecino not in visitados:
                    cola_bfs.append(vecino)
    print("No existe camino entre las zonas.")
    return False


def dijkstra(origen, destino):
    if origen not in grafo or destino not in grafo:
        print("Zona no encontrada en el grafo.")
        return None, None

    distancias = {zona: float("inf") for zona in grafo}
    distancias[origen] = 0
    anteriores = {zona: None for zona in grafo}
    visitados = []

    while len(visitados) < len(grafo):
        actual = None
        menor = float("inf")
        for zona in grafo:
            if zona not in visitados and distancias[zona] < menor:
                menor = distancias[zona]
                actual = zona
        if actual is None:
            break

        print(f"Nodo actual: {actual}")
        visitados.append(actual)

        for vecino, peso in grafo[actual]:
            nueva_distancia = distancias[actual] + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual

        print("Distancias:", distancias)

        ruta_parcial = []
        nodo = actual
        while nodo is not None:
            ruta_parcial.insert(0, nodo)
            nodo = anteriores[nodo]
        print("Ruta parcial:", ruta_parcial)

    if distancias[destino] == float("inf"):
        print("No existe ruta hacia el destino.")
        return None, None

    ruta_final = []
    nodo = destino
    while nodo is not None:
        ruta_final.insert(0, nodo)
        nodo = anteriores[nodo]

    print("Ruta final:", ruta_final)
    print("Distancia total:", distancias[destino])
    return ruta_final, distancias[destino]


def buscar_dron_disponible():
    for d in drones:
        if d["estado"] == "Disponible":
            return d
    return None


def simulacion_rescate():
    print(" \n     INICIANDO SIMULACIÓN DE RESCATE      ")

    print("\n[Fase 1] Registro e Inserción")
    mision = registrar_mision()
    if not mision:
        print(">> Simulación cancelada: Error al registrar la misión.")
        return

    print(" Misión insertada correctamente en el árbol de búsqueda (BST).")
    
    print("\n[Fase 2] Optimización de Prioridades")
    burbuja_prioridad()
    print(">> Lista de misiones reordenadas exitosamente.")
    
    print("\n[Fase 3] Selección de Recursos")
    dron = buscar_dron_disponible()
    if not dron:
        print("Error: No se encontraron drones en estado 'Disponible'.")
        return
    print(f">> Dron asignado para la operación: {dron['codigo']}")
    
    print("\n[Fase 4] Análisis de Viabilidad de Ruta (BFS)")
    origen = "Base"
    if origen not in grafo:
        print(f"Error: La zona '{origen}' no está registrada en el sistema de mapas.")
        return
        
    if not bfs_existe_camino(origen, mision["zona"]):
        print(f"Error: No existe conexión hacia '{mision['zona']}'.")
        return
    print(f" Existe una ruta válida hacia '{mision['zona']}'.")
    
    print("\n[Fase 5] Cálculo de Ruta Óptima (Dijkstra)")
    ruta, distancia_total = dijkstra(origen, mision["zona"])
    if ruta is None:
        print(">> Error: No se pudo trazar la ruta.")
        return
        
    print("\n[Fase 6] Despliegue y Actualización de Estados")
    dron["estado"] = "En misión"
    mision["estado"] = "Asignada"
    
    if mision in cola_misiones:
        cola_misiones.remove(mision)
        
    print("-" * 40)
    print(f"Opreación inicializada")
    print(f"Misión: {mision['codigo']} ---> Dron: {dron['codigo']}")
    print(f"Plan de Vuelo: {' -> '.join(ruta)}")
    print(f"Distancia Total: {distancia_total} km")
    print("Simulación finalizada exitosamente.")


def menu_drones():
    while True:
        print("\n--- DRONES ---")
        print("\n1. Registrar dron")
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


def org_misiones():
    while True:
        print("\n---Organización de misiones---")
        print("\n1. Ordenar misiones por prioridad (Burbuja)")
        print("2. Ordenar drones por batería (Inserción)")
        print("3. Ordenar drones por velocidad (MergeSort)")
        print("4. Ordenar misiones por distancia (QuickSort)")
        print("5. Volver")
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                burbuja_prioridad()
            case "2":
                insercion_bateria()
            case "3":
                mergesort_velocidad()
            case "4":
                quicksort_distancia()
            case "5":
                return
            case _:
                print("Opción inválida.")


def menu_misiones():
    while True:
        print("\n--- MISIONES ---")
        print("\n1. Registrar misión")
        print("2. Mostrar misiones")
        print("3. Eliminar misión")
        print("4. Atender siguiente misión")
        print("5. Mostrar siguiente misión")
        print("6. Registrar zona")
        print("7. Registrar ruta entre zonas")
        print("8. Mostrar grafo de zonas")
        print("9. Regresar al menú principal")
        opcion = input("\nIngrese una opción válida: ")
        match opcion:
            case "1":
                registrar_mision()
            case "2":
                mostrar_misiones()
            case "3":
                eliminar_mision()
            case "4":
                atender_mision()
            case "5":
                mostrar_siguiente_mision()
            case "6":
                registrar_zona()
            case "7":
                registrar_ruta()
            case "8":
                mostrar_grafo()
            case "9":
                return
            case _:
                print("Opción inválida.")


def menu_algoritmos():
    while True:
        print("\n--- ALGORITMOS DE BÚSQUEDA Y RUTAS ---")
        print("\n1. Búsqueda lineal de dron")
        print("2. Búsqueda lineal de misión")
        print("3. Búsqueda binaria de dron")
        print("4. Verificar camino entre zonas (BFS)")
        print("5. Calcular ruta mínima (Dijkstra)")
        print("6. Volver")
        opcion = input("\nIngrese una opcion: ")
        match opcion:
            case "1":
                busqueda_lineal_dron()
            case "2":
                busqueda_lineal_mision()
            case "3":
                busqueda_binaria_dron()
            case "4":
                origen = input("Zona origen: ")
                destino = input("Zona destino: ")
                bfs_existe_camino(origen, destino)
            case "5":
                origen = input("Zona origen: ")
                destino = input("Zona destino: ")
                dijkstra(origen, destino)
            case "6":
                return
            case _:
                print("Opción inválida.")


def menu_registrar():

    while True:
        print("\n--- REGISTRAR INFORMACIÓN ---")
        print("\n1. Drones")
        print("2. Misiones")
        print("3. Volver")
        opcion = input("\nIngrese una opción: ")
        match opcion:
            case "1":
                menu_drones()
            case "2":
                menu_misiones()
            case "3":
                return
            case _:
                print("Opción inválida.")


def menu_principal():
    while True:
        print("\nPOLIRESCUE TECHNOLOGIES ")

        print("\n1. Registrar información ")
        print("2. Árbol BST de misiones")
        print("3. Organización de misiones")
        print("4. Algoritmos de búsqueda y rutas")
        print("5. Simulación completa de rescate")
        print("0. Salir")

        opcion = input("\nSeleccione: ")

        match opcion:
            case "1":
                menu_registrar()
            case "2":
                menu_bst()
            case "3":
                org_misiones()
            case "4":
                menu_algoritmos()
            case "5":
                simulacion_rescate()
            case "0":
                print("Saliendo del sistema.....")
                break
            case _:
                print("Opción inválida.")


menu_principal()
