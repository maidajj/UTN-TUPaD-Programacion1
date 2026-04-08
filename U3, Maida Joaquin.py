#Ejercicio 1
while True:
    nombre = input("¿Cuál es su nombre? ")
    if nombre.isalpha():
        break
    else:
        print("Ingrese un nombre válido")

while True:
    productos = input("Cantidad de productos: ")
    if productos.isdigit() and int(productos) > 0:
        productos = int(productos)
        break
    else:
        print("Ingrese un número positivo")

total_sin_descuento = 0
total_con_descuento = 0

for i in range(productos):
    while True:
        precio = input(f"Producto {i+1} - Precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error: ingrese un número válido.")

    total_sin_descuento += precio

    while True:
        descuento = input(" Descuento (S/N): ").lower()
        if descuento == "s" or descuento == "n":
            break
        else:
            print("Error: ingrese S o N.")

    if descuento == "s":
        precio_con_desc = precio * 0.9
    else:
        precio_con_desc = precio

    total_con_descuento += precio_con_desc

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / productos

print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


#Ejercicio 2
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
login_ok = False

while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        login_ok = True
        print("Acceso concedido")
        break
    else:
        intentos += 1
        print("Credenciales inválidas")

if not login_ok:
    print("Cuenta bloqueada")
else:
    while True:
        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango")
            continue

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            while True:
                nueva = input("Nueva clave: ")
                if len(nueva) < 6:
                    print("Error: minimo 6 caracteres")
                    continue
                
                confirmacion = input("Confirmar clave: ")

                if nueva == confirmacion:
                    clave_correcta = nueva
                    print("Clave actualizada correctamente")
                    break
                else:
                    print("Error: las claves no coinciden")

        elif opcion == 3:
            print("Enhorabuena!")

        elif opcion == 4:
            print("Saliendo del sistema...")
            break


#Ejercicio 3
while True:
    nombre = input("Ingrese su nombre: ")
    if nombre.isalpha():
        break
    else:
        print("Solo se admiten letras.")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    print("\nMenú")
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema ")

    opcion = input("Opción: ")

    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción inválida")
        continue

    opcion = int(opcion)

    if opcion == 1:
        dia = input("Seleccione el dia del turno: 1-Lunes 2-Martes ")
        if dia != "1" and dia != "2":
            print("Error: día inválido")
            continue

        while True:
            nombre_turno = input("Nombre del paciente: ")
            if nombre_turno.isalpha():
                break
            else:
                print("Error: solo se admiten letras.")

        if dia == "1":
            if nombre_turno == lunes1 or nombre_turno == lunes2 or nombre_turno == lunes3 or nombre_turno == lunes4:
                print("El paciente ya tiene turno ese dia")
            else:
                if lunes1 == "":
                    lunes1 = nombre_turno
                elif lunes2 == "":
                    lunes2 = nombre_turno
                elif lunes3 == "":
                    lunes3 = nombre_turno
                elif lunes4 == "":
                    lunes4 = nombre_turno
                else:
                    print("No se encuentran turnos disponibles.")
        else:
            if nombre_turno == martes1 or nombre_turno == martes2 or nombre_turno == martes3:
                print("El paciente ya tiene turno ese dia")
            else:
                if martes1 == "":
                    martes1 = nombre_turno
                elif martes2 == "":
                    martes2 = nombre_turno
                elif martes3 == "":
                    martes3 = nombre_turno
                else:
                    print("No se encuentran turnos disponibles.")

    elif opcion == 2:
        dia = input("Seleccione el dia del turno: 1-Lunes 2-Martes ")
        if dia != "1" and dia != "2":
            print("Error: día inválido")
            continue

        while True:
            nombre_turno = input("Nombre del paciente: ")
            if nombre_turno.isalpha():
                break
            else:
                print("Error: solo se admiten letras.")

        encontrado = False

        if dia == "1":
            if lunes1 == nombre_turno:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre_turno:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre_turno:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre_turno:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == nombre_turno:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre_turno:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre_turno:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado")
        else:
            print("Paciente no encontrado")

    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("Lunes:")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        elif dia == "2":
            print("Martes:")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")
        else:
            print("Error: día inválido")

    elif opcion == 4:
        print("Resumen general:")
        print("Lunes:", lunes1 or "(libre)", lunes2 or "(libre)", lunes3 or "(libre)", lunes4 or "(libre)")
        print("Martes:", martes1 or "(libre)", martes2 or "(libre)", martes3 or "(libre)")

    elif opcion == 5:
        print("Cerrando sistema...")
        break

#Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0

nombre = input("Ingrese nombre del agente: ")
while not nombre.isalpha():
    nombre = input("Error: Ingrese solo letras: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("DERROTA POR BLOQUEO")
        break

    print("\nESTADO")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")
    print(f"Codigo parcial: {codigo_parcial}")

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione una opcion: ")
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        opcion = input("Opción inválida.")

    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            alarma = True
            print("La cerradura se trabo. ALARMA ACTIVADA")
            continue

        if energia < 40:
            riesgo = input("Riesgo de alarma. Elegí un número del 1 al 3: ")
            while not riesgo.isdigit() or int(riesgo) not in [1, 2, 3]:
                riesgo = input("Numero invalido. Ingrese 1, 2 o 3: ")

            if int(riesgo) == 3:
                alarma = True
                print("Se activo la alarma")

        if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("Hackeando...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Código completo. Se abrió una cerradura")

    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        racha_forzar = 0

        if alarma:
            energia -= 10

        print("Descansaste")

if cerraduras_abiertas == 3:
    print("VICTORIA")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")

#Ejercicio 5
print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# VARIABLES INICIALES
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_jugador = 15
danio_enemigo = 12

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1) Ataque Pesado")
    print("2) Ráfaga Veloz")
    print("3) Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        if vida_enemigo < 20:
            danio = danio_jugador * 1.5   # float
            print("¡Golpe Crítico!")
        else:
            danio = danio_jugador

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te curaste 30 HP")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

    print("=== NUEVO TURNO ===")

if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")