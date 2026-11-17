# Sistema de reservas de talleres comunitarios
# Definición de funciones
def mostrar_menu():
    print("===MENÚ PRINCIPAL===")
    print("1. Registrar sesión de taller.")
    print("2. Mostrar sesiones registradas.")
    print("3. Inscribir participante en una sesión abierta.")
    print("4. Cerrar inscripciones de una sesión")
    print("5. Buscar sesiones por nombre de taller")
    print("6. Mostrar estadísticas y la clasificación.")
    print("7. Salir.")
    
def solicitar_entero_rango(mensaje,minimo,maximo):
    validado = False
    try:
        num = int(input(mensaje))
        if maximo > minimo:
            if num >= minimo and num <= maximo:
                validado = True
            else:
                print(f"¡Número ingresado inválido! Debe ingresar un valor entre {minimo} y {maximo}.")
        else:
            if num >= minimo:
                validado = True
            else:
                print(f"¡Valor ingresado inválido! Debe ingresar un valor mayor o igual a {minimo}.")
    except ValueError:
        print(f"¡Valor ingresado inválido! Debe ingresar un valor entero.")

    return validado,num

def solicitar_texto(mensaje,largo_minimo):
    validado = False
    validado_largo = False
    validado_espacio = False
    contador_espacios = 0
    texto = input(mensaje)
    for caracter in texto:
        if caracter == " ":
            contador_espacios += 1
    
    if contador_espacios != len(texto):
        validado_espacio = True
        if len(texto) >= largo_minimo:
            validado_largo = True
        else:
            print(f"¡Texto ingresado inválido! Debe tener al menos {largo_minimo} caracteres.")
    else:
        print(f"¡Texto ingresado inválido! No puede quedar vacío.")
    
    validado = validado_largo and validado_espacio
    return validado,texto

def normalizar_texto(texto):
    texto = texto.strip()
    texto = texto.upper()
    return texto

def registrar_sesion(sesiones,talleres):
    codigo = input("Ingrese el código del taller: ").upper()
    while codigo not in talleres:
        print("¡El código ingresado no existe!")
        codigo = input("Ingrese el código del taller: ").upper()

    validado = False
    while not validado:
        mensaje = "Ingrese el nombre del monitor: "
        validado,nombre=solicitar_texto(mensaje,3)

    nombre = normalizar_texto(nombre)
    nombre = nombre.upper()

    validado = False
    while not validado:
        mensaje = "Ingrese el cupo máximo de inscritos para el taller: "
        validado,cupo = solicitar_entero_rango(mensaje,1,40)

    identificador = len(sesiones) + 101
    total_inscritos = 0

    datos = {
        "id":identificador,
        "codigo":codigo,
        "monitor":nombre,
        "cupo_max":cupo,
        "inscritos":[],
        "estado":"ABIERTA",
        "total_inscritos":total_inscritos
    }

    validado = False
    while not validado:
        mensaje = "¿Desea inscribir participantes? (1. Si, 2. No): "
        validado,agregar = solicitar_entero_rango(mensaje,1,2)

    if agregar == 1:
        validado = False
        while not validado:
            mensaje = "Ingrese la cantidad de participantes a inscribir: "
            validado,cantidad = solicitar_entero_rango(mensaje,1,cupo)

        for participantes in range(cantidad):
            validado = False
            while not validado:
                mensaje = "Ingrese el nombre del participante: "
                validado,nom_participante = solicitar_texto(mensaje,3)

            validado = False
            while not validado:
                mensaje = "Ingrese la edad del participante: "
                validado,edad = solicitar_entero_rango(mensaje,12,100)

            inscribir_participante(datos["inscritos"],nom_participante,edad,cupo)
            cupo = cupo - 1
            total_inscritos = total_inscritos + 1
        sesiones.append(datos)
    else:
        sesiones.append(datos)

def mostrar_sesiones(sesiones,talleres):
    if len(sesiones) > 0:
        for taller in talleres:
            nombre = talleres[f"{taller}"]
            print(f"Taller de {nombre}")
            for indice in range(len(sesiones)):
                if sesiones[indice]["codigo"] == taller:
                    print(f"ID: {sesiones[indice]["id"]}")
                    print(f"Monitor: {sesiones[indice]["monitor"]}")
                    print(f"Estado: {sesiones[indice]["estado"]}")
                    print(f"cupos ocupados: {len(sesiones[indice]["inscritos"])}")
                    print(f"Cupos disponibles: {sesiones[indice]["cupo_max"] - len(sesiones[indice]["inscritos"])}")

def inscribir_participante(inscritos,nombre,edad,cupo_max):
    total_inscritos = len(inscritos)
    restantes = cupo_max - total_inscritos
    if restantes > 0:
        inscribir = True
        for indice in range(total_inscritos):
            if inscritos[indice]["nombre"] == nombre:
                if inscritos[indice]["edad"] == edad:
                    inscribir = False

        if inscribir:
            datos = {
                "nombre":nombre,
                "edad":edad,
            }
            inscritos.append(datos)
        else:
            print("Lo sentimos, el participante ya figura como inscrito.")
    else:
        print("Lo sentimos, no quedan cupos disponibles para realizar la inscripción.")

def cerrar_sesion(sesiones,identificador):
    if len(sesiones) > 0:
        encontrado,pos = buscar_sesion(sesiones,identificador)

        if encontrado:
            if sesiones[pos]["estado"] == "CERRADA":
                print("La sesión ya se encuentra cerrada.")
            else:
                sesiones[pos]["estado"] == "CERRADA"
        else:
            print("Lo sentimos, no se encontraron coincidencias de id.")

def buscar_sesion(sesiones,identificador):
    if len(sesiones) > 0:
        while not validado:
            mensaje = "Ingrese el id de la sesión: "
            validado,identificador = solicitar_entero_rango(mensaje,100,0)
        
            encontrado = False
            pos = 0
            for indice in range(len(sesiones)):
                if sesiones[indice]["id"] == identificador:
                    encontrado = True
                    pos = indice
    return encontrado,pos

#def 
    

        

talleres = {
    "CER":"Cerámica",
    "FOT":"Fotografía",
    "TEA":"Teatro"
}

sesiones = []
registrar_sesion(sesiones,talleres)
print(sesiones)