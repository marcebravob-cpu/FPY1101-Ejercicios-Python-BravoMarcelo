# Sistema de solicitudes de mantenimiento de jardines urbanos
# Definición de funciones
def mostrar_menu():
    print("===MENÚ PRINCIPAL===")
    print("1. Registrar solicitud de mantenimiento.")
    print("2. Buscar solicitudes pendientes.")
    print("3. Buscar solicitudes por palabra clave.")
    print("4. Finalizar solicitud.")
    print("5. Mostrar resumen por tipo de trabajo y estado.")
    print("6. Salir.")
    
def solicitar_entero(mensaje,minimo,maximo):
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
                print(f"¡Número ingresado inválido! Debe ingresar un valor mayor o igual a {minimo}.")
    except ValueError:
        print(f"¡Número ingresado inválido! Debe ingresar un valor entero.")

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
    texto = texto.lower()
    return texto

def verificar_fecha():
    validado = False
    while not validado:
        mensaje = "Ingrese la fecha (DD-MM-AAAA): "
        validado,fecha = solicitar_texto(mensaje,10)
    
    contador = fecha.count("-")
    validado_3 = False
    validado_1 = False
    validado_2 = False
    if len(fecha) == 10:
        if contador == 2:
            lista = fecha.split("-")
            for indice in range(len(lista)):
                if indice != 2:
                    if len(lista[indice]) == 2:
                        validado_1 = True
                    else:
                        print("¡Fecha ingresada inválida! No cumple con el formato DD-MM-AAA.")
                        break
                else:
                    if len(lista[indice]) == 4:
                        validado_2 = True
                    else:
                        print("¡Fecha ingresada inválida! No cumple con el formato DD-MM-AAA.")
                        break
                        
            validado_3 = validado_1 and validado_2
        else:
            print("¡Fecha ingresada inválida! No cumple con el formato DD-MM-AAA.")
    else:
        print("¡Fecha ingresada inválida! Debe tener exactamente 10 caracteres.")
    
    return validado_3,fecha

def registrar_solicitud(solicitudes,tipo):
    validado = False
    while not validado:
        mensaje_desc = "Ingrese una descripción: "
        validado,desc = solicitar_texto(mensaje_desc,5)
    desc = normalizar_texto(desc)
    print(desc)
    
    servicio =  input("Ingrese el tipo de servicio (Poda, Riego, Limpieza): ").title()
    while servicio not in tipo:
        print("¡El servicio ingresado no existe!")
        servicio =  input("Ingrese el tipo de servicio (Poda, Riego, Limpieza): ").title()
        
    validado = False
    while not validado:
        validado,fecha = verificar_fecha()
    fecha = normalizar_texto(fecha)
    print(fecha)
    
    identificador = len(solicitudes) + 101
    
    datos = {
        "id":identificador,
        "descripción":desc,
        "tipo":servicio,
        "fecha":fecha,
        "estado":"PENDIENTE",
        "encargado": "NINGUNO"
    }
    
    solicitudes.append(datos)

def mostrar_pendientes(solicitudes):
    print("===SOLICITUDES PENDIENTES===")
    encontrado = False
    if len(solicitudes) > 0:
        for indice in range(len(solicitudes)):
            if solicitudes[indice]["estado"] == "PENDIENTE":
                encontrado = True
                print(f"ID: {solicitudes[indice]["id"]}")
                print(f"Descripción: {solicitudes[indice]["descripción"]}")
                print(f"Tipo: {solicitudes[indice]["tipo"]}")
                print(f"Fecha: {solicitudes[indice]["fecha"]}")
        if not encontrado:
            print("No hay solicitudes pendientes.")
        print("***********************************************************")
    else:
        print("Aún no se han hecho solicitudes.")
        print("***********************************************************")

def buscar_solicitudes(solicitudes):
    print("===BUSCAR SOLICITUDES===")
    if len(solicitudes) > 0:
        validado = False
        while not validado:
            mensaje = "Ingrese palabra clave: "
            validado,palabra = solicitar_texto(mensaje,5)
        
        palabra = normalizar_texto(palabra)
        encontrado = False
        pos = 0
        for indice in range(len(solicitudes)):
            if palabra in solicitudes[indice]["descripción"]:
                encontrado = True
                pos = indice
        
        if encontrado:
            print(f"ID: {solicitudes[pos]["id"]}")
            print(f"Descripción: {solicitudes[pos]["descripción"]}")
            print(f"Tipo: {solicitudes[pos]["tipo"]}")
            print(f"Fecha: {solicitudes[pos]["fecha"]}")
            print(f"Estado: {solicitudes[pos]["estado"]}")
            print(f"Encargado: {solicitudes[pos]["encargado"]}")
        else:
            print("No se encontraron coincidencias.")
        print("***********************************************************")
    else:
        print("Lo sentimos, aún no se han hecho solicitudes.")
        print("***********************************************************")

def finalizar_solicitud(solicitudes):
    print("===FINALIZAR SOLICITUD===")
    if len(solicitudes) > 0:
        validado = False
        while not validado:
            mensaje_id = "Ingrese el id de la solicitud: "
            validado,num = solicitar_entero(mensaje_id,100,0)
        
        validado = False
        while not validado:
            mensaje_encargado = "Ingrese el nombre del encargado: "
            validado,nombre = solicitar_texto(mensaje_encargado,3)
        
        nombre = normalizar_texto(nombre)
        nombre = nombre.title()
        encontrado = False
        pos = 0
        for indice in range(len(solicitudes)):
            if solicitudes[indice]["id"] == num:
                encontrado = True
                pos = indice
        
        if encontrado:
            solicitudes[pos]["estado"] = "FINALIZADA"
            solicitudes[pos]["encargado"] = nombre
        else:
            print("No se encontraron coincidencias.")
        print("***********************************************************")
    else:
        print("Lo sentimos, aún no se han hecho solicitudes.")
        print("***********************************************************")

def mostrar_resumen(solicitudes,tipos):
    print("===RESUMEN===")
    if len(solicitudes) > 0:
        for tipo in tipos:
            print(f"Tipo: {tipo}")
            total_pendientes = 0
            total_finalizadas = 0
            finalizacion = 0
            for indice in range(len(solicitudes)):
                if solicitudes[indice]["tipo"] == tipo:
                    if solicitudes[indice]["estado"] == "PENDIENTE":
                        total_pendientes += 1
                    else:
                        total_finalizadas = total_finalizadas + 1
            
            total = total_pendientes + total_finalizadas
            if total > 0:
                finalizacion = (total_finalizadas/total)*100
            else:
                finalizacion = 0

            print(f"Total de solicitudes: {total}")
            print(f"Total de solicitudes pendientes: {total_pendientes}")
            print(f"Total de solicitudes finalizadas: {total_finalizadas}")
            print(f"Porcentaje de finalización: {round(finalizacion)}%")
            print("***********************************************************")
    else:
        print("Lo sentimos, aún no se han hecho solicitudes.")
        print("***********************************************************")

# Ciclo principal
solicitudes = []
tipos = ["Poda","Riego","Limpieza"]
menu = True
while menu:
    mostrar_menu()
    validado = False
    while not validado:
        mensaje_decision = "Seleccione una opción: "
        validado,decision = solicitar_entero(mensaje_decision,1,6)
    
    if decision == 1:
        registrar_solicitud(solicitudes,tipos)
    
    elif decision == 2:
        mostrar_pendientes(solicitudes)
    
    elif decision == 3:
        buscar_solicitudes(solicitudes)
    
    elif decision == 4:
        finalizar_solicitud(solicitudes)
    
    elif decision == 5:
        mostrar_resumen(solicitudes,tipos)
    
    elif decision == 6:
        print("Fin del programa.")
        break