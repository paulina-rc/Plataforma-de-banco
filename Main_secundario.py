from collections import deque

cola_prioridad1 = deque()
cola_prioridad2 = deque()

clientes_en_cola = set()

cajas = {
    1: {"estado": "activa", "cliente": None, "pila": []},
    2: {"estado": "activa", "cliente": None, "pila": []},
    3: {"estado": "activa", "cliente": None, "pila": []}
}

def mostrar_cola():
    print("\nEstado de la cola:")
    for c in list(cola_prioridad1) + list(cola_prioridad2):
        print(f"Cédula: {c['cedula']} | Nombre: {c['nombre']} | Trámite: {c['tramite']} | Prioridad: {c['prioridad']}")
    print("-" * 40)

def ingresar_cliente():
    cedula = input("Cédula: ")

    if cedula in clientes_en_cola:
        print("Error: Cédula ya existe en la cola")
        return

    nombre = input("Nombre: ")
    tramite = input("Trámite: ")
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

    clientes_en_cola.add(cedula)

    asignar_clientes()
    mostrar_cola()

def asignar_clientes():
    for num, caja in cajas.items():
        if caja["estado"] == "activa" and caja["cliente"] is None:
            cliente = obtener_siguiente_cliente()
            if cliente:
                caja["cliente"] = cliente

def obtener_siguiente_cliente():
    if cola_prioridad1:
        cliente = cola_prioridad1.popleft()
    elif cola_prioridad2:
        cliente = cola_prioridad2.popleft()
    else:
        return None

    clientes_en_cola.remove(cliente["cedula"])
    return cliente

def terminar_atencion():
    num = int(input("Número de caja: "))

    if cajas[num]["cliente"] is None:
        print("No hay cliente en esa caja")
        return

    cliente = cajas[num]["cliente"]
    cajas[num]["pila"].append(cliente)
    print(f"Cliente atendido: {cliente['nombre']}")

    cajas[num]["cliente"] = None

    asignar_clientes()
    mostrar_cola()

def cambiar_estado_caja():
    num = int(input("Número de caja: "))

    if cajas[num]["estado"] == "activa":
        cajas[num]["estado"] = "inactiva"
    else:
        cajas[num]["estado"] = "activa"

    print(f"Caja {num} ahora está {cajas[num]['estado']}")
    asignar_clientes()

def ver_estado_cajas():
    print("\nEstado de cajas:")
    for num, caja in cajas.items():
        if caja["estado"] == "inactiva":
            print(f"Caja {num}: INACTIVA")
        elif caja["cliente"]:
            c = caja["cliente"]
            print(f"Caja {num}: OCUPADA con {c['nombre']}")
        else:
            print(f"Caja {num}: LIBRE")

def ver_ultimas_atenciones_caja():
    num = int(input("Caja: "))
    x = int(input("Cantidad: "))

    pila = cajas[num]["pila"][-x:]

    print("\nÚltimas atenciones:")
    for c in reversed(pila):
        print(c)

def ver_ultimas_atenciones_todas():
    x = int(input("Cantidad: "))
    todas = []

    for caja in cajas.values():
        todas.extend(caja["pila"])

    ultimas = todas[-x:]

    print("\nÚltimas atenciones globales:")
    for c in reversed(ultimas):
        print(c)

def informe_prioridad():
    p = int(input("Prioridad: "))
    contador = 0

    for caja in cajas.values():
        for c in caja["pila"]:
            if c["prioridad"] == p:
                contador += 1

    print(f"Total atendidos con prioridad {p}: {contador}")

def informe_detallado():
    p = int(input("Prioridad: "))

    print("\nClientes atendidos:")
    for caja in cajas.values():
        for c in caja["pila"]:
            if c["prioridad"] == p:
                print(f"{c['nombre']} - {c['tramite']}")

def menu():
    while True:
        print("""
            1. Ingresar cliente
            2. Terminar atención
            3. Activar/Desactivar caja
            4. Ver últimas atenciones de una caja
            5. Ver últimas atenciones de todas
            6. Informe cantidad por prioridad
            7. Informe detallado por prioridad
            8. Ver cola
            9. Ver estado de cajas
            0. Salir
        """)

        opcion = input("Seleccione: ")

        if opcion == "1":
            ingresar_cliente()
        elif opcion == "2":
            terminar_atencion()
        elif opcion == "3":
            cambiar_estado_caja()
        elif opcion == "4":
            ver_ultimas_atenciones_caja()
        elif opcion == "5":
            ver_ultimas_atenciones_todas()
        elif opcion == "6":
            informe_prioridad()
        elif opcion == "7":
            informe_detallado()
        elif opcion == "8":
            mostrar_cola()
        elif opcion == "9":
            ver_estado_cajas()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

menu()