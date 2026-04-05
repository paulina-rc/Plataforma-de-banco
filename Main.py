cola_prioridad1 = []
cola_prioridad2 = []

cajas = {
    1: {"estado": "activa", "cliente": None, "pila": []},
    2: {"estado": "activa", "cliente": None, "pila": []},
    3: {"estado": "activa", "cliente": None, "pila": []}
}


def validar_cedula(cedula):
    for cliente in cola_prioridad1:
        if cliente["cedula"] == cedula:
            return False

    for cliente in cola_prioridad2:
        if cliente["cedula"] == cedula:
            return False

    return True


def ingresar_cliente():
    cedula = input("Cedula: ")

    if validar_cedula(cedula) == False:
        print("Cedula ya existe")
        return

    nombre = input("Nombre: ")
    tramite = input("Tramite: ")
    prioridad = int(input("Prioridad (1 o 2): "))

    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "tramite": tramite,
        "prioridad": prioridad
    }

    if prioridad == 1:
        cola_prioridad1.append(cliente)
    else:
        cola_prioridad2.append(cliente)

    print("Cliente agregado")

    asignar_cliente()
    mostrar_cola()


def mostrar_cola():
    print("\n--- COLA ---")

    if len(cola_prioridad1) == 0 and len(cola_prioridad2) == 0:
        print("No hay clientes")
        return

    print("Prioridad 1:")
    for cliente in cola_prioridad1:
        print(cliente["cedula"], cliente["nombre"], cliente["tramite"], cliente["prioridad"])

    print("Prioridad 2:")
    for cliente in cola_prioridad2:
        print(cliente["cedula"], cliente["nombre"], cliente["tramite"], cliente["prioridad"])


def asignar_cliente():

    # caja 1
    if cajas[1]["estado"] == "activa" and cajas[1]["cliente"] == None:
        if len(cola_prioridad1) > 0:
            cajas[1]["cliente"] = cola_prioridad1.pop(0)
        elif len(cola_prioridad2) > 0:
            cajas[1]["cliente"] = cola_prioridad2.pop(0)

    # caja 2
    if cajas[2]["estado"] == "activa" and cajas[2]["cliente"] == None:
        if len(cola_prioridad1) > 0:
            cajas[2]["cliente"] = cola_prioridad1.pop(0)
        elif len(cola_prioridad2) > 0:
            cajas[2]["cliente"] = cola_prioridad2.pop(0)

    # caja 3
    if cajas[3]["estado"] == "activa" and cajas[3]["cliente"] == None:
        if len(cola_prioridad1) > 0:
            cajas[3]["cliente"] = cola_prioridad1.pop(0)
        elif len(cola_prioridad2) > 0:
            cajas[3]["cliente"] = cola_prioridad2.pop(0)


def terminar_atencion():
    num = int(input("Caja (1-3): "))

    if num < 1 or num > 3:
        print("Caja invalida")
        return

    if cajas[num]["cliente"] == None:
        print("No hay cliente")
        return

    cajas[num]["pila"].append(cajas[num]["cliente"])

    print("Cliente atendido:", cajas[num]["cliente"]["nombre"])

    cajas[num]["cliente"] = None

    asignar_cliente()


def cambiar_estado_caja():
    num = int(input("Caja (1-3): "))

    if cajas[num]["estado"] == "activa":
        cajas[num]["estado"] = "inactiva"
        print("Caja desactivada")
    else:
        cajas[num]["estado"] = "activa"
        print("Caja activada")

    asignar_cliente()



def ver_cajas():
    print("CAJAS")

    for i in range(1, 4):
        print("Caja", i, "-", cajas[i]["estado"])

        if cajas[i]["cliente"] != None:
            c = cajas[i]["cliente"]
            print("Cliente:", c["nombre"], c["tramite"])
        else:
            print("Libre")



def ultimas_caja():
    num = int(input("Caja: "))
    x = int(input("Cantidad: "))

    pila = cajas[num]["pila"]

    i = len(pila) - 1
    contador = 0

    while i >= 0 and contador < x:
        c = pila[i]
        print(c["nombre"], c["tramite"])
        i = i - 1
        contador = contador + 1


def ultimas_todas():
    x = int(input("Cantidad: "))

    lista = []

    for i in range(1, 4):
        for c in cajas[i]["pila"]:
            lista.append(c)

    i = len(lista) - 1
    contador = 0

    while i >= 0 and contador < x:
        c = lista[i]
        print(c["nombre"], c["tramite"])
        i = i - 1
        contador = contador + 1


def reporte_cantidad():
    p = int(input("Prioridad: "))
    total = 0

    for i in range(1, 4):
        for c in cajas[i]["pila"]:
            if c["prioridad"] == p:
                total = total + 1

    print("Total:", total)



def reporte_detalle():
    p = int(input("Prioridad: "))

    for i in range(1, 4):
        for c in cajas[i]["pila"]:
            if c["prioridad"] == p:
                print(c["nombre"], c["tramite"])

while True:
    print("\nMENU")
    print("1. Ingresar cliente")
    print("2. Terminar atencion")
    print("3. Activar/Desactivar caja")
    print("4. Ver cola")
    print("5. Ver cajas")
    print("6. Ultimas por caja")
    print("7. Ultimas generales")
    print("8. Reporte cantidad")
    print("9. Reporte detalle")
    print("0. Salir")

    op = input("Opcion: ")

    if op == "1":
        ingresar_cliente()
    elif op == "2":
        terminar_atencion()
    elif op == "3":
        cambiar_estado_caja()
    elif op == "4":
        mostrar_cola()
    elif op == "5":
        ver_cajas()
    elif op == "6":
        ultimas_caja()
    elif op == "7":
        ultimas_todas()
    elif op == "8":
        reporte_cantidad()
    elif op == "9":
        reporte_detalle()
    elif op == "0":
        break
                    

