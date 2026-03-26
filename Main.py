cola_prioridad1 = []
cola_prioridad2 = []

cajas = {
    1: {"estado": "activa", "cliente": None, "pila": []},
    2: {"estado": "activa", "cliente": None, "pila": []},
    3: {"estado": "activa", "cliente": None, "pila": []}
}

def ingresar_cliente():
     
    cedula = input("Cedula:")
    nombre = input("Nombre:")
    tramite = input("Tramite por el que viene: ")
    prioridad = int(input("Prioridad (1 o 2)"))

    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "tramite": tramite,
        "prioridad": prioridad
    }

    if prioridad == 1:
        if validar_cedula(cedula):
            cola_prioridad1.append(cliente)
            print("Cliente registrado")
            mostrar_cola()
        else:
            print("Cedula ya registrada")
    else:
        if validar_cedula(cedula):
            cola_prioridad2.append(cliente)
            print("Cliente registrado")
            mostrar_cola()
        else:
            print("Cedula ya registrada") 


def validar_cedula(cedula):
    for cliente in cola_prioridad1 + cola_prioridad2:
        if cliente["cedula"] == cedula:
            return False
    return True 

def mostrar_cola():

    if not cola_prioridad1 and not cola_prioridad2:
        print("no hay clienten en espera")
        return
    
    print("Clientes de prioridad 1 en espera")
    for cliente in cola_prioridad1:
        print(cliente["nombre"], " ", cliente["tramite"])

    print("Clientes de prioridad 2 en espera")
    for cliente in cola_prioridad2:
        print(cliente["nombre"], " ", cliente["tramite"])





#Pruebas 
while True:
       print("1 ingrese el cliente")
       print("2 salir ")
       print("3 mostrar cola")
       opcion = input("Numero:")

       if opcion == "1":
           ingresar_cliente()

       elif opcion == "2":
           break
       
       elif opcion == "3":
           mostrar_cola()
                    

