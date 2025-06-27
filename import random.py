import random  
import string

NIVELES = ("Débil", "Media", "Fuerte")
historial = []
MAX_INTENTOS = 3

# Variable global para el nombre del usuario
usuario_actual = ""

def obtener_nombre_usuario():
    global usuario_actual
    usuario_actual = input("Por favor, ingrese su nombre de usuario: ").strip().capitalize()
    print(f"\n¡Hola, {usuario_actual}! Comencemos...\n")

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Ver Reglas del Juego")
    print("2. Generar Contraseña Automáticamente")
    print("3. Crear Contraseña Manualmente")
    print("4. Ver Historial de Contraseñas")
    print("5. Salir")

def mostrar_reglas():
    print("\n--- Reglas del Juego ---")
    print("Tu objetivo es generar contraseñas seguras.")
    print("Puedes dejar que el sistema la genere o escribir una tú mismo.")
    print("La contraseña será evaluada y clasificada por seguridad.")
    print(f"Puedes probar hasta {MAX_INTENTOS} contraseñas por ronda manual, luego puedes volver al menú.")

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def evaluar_contraseña(contraseña):
    puntaje = 0
    if len(contraseña) >= 8:
        puntaje += 2
    if any(c.islower() for c in contraseña):
        puntaje += 2
    if any(c.isupper() for c in contraseña):
        puntaje += 2
    if any(c.isdigit() for c in contraseña):
        puntaje += 2
    if any(c in string.punctuation for c in contraseña):
        puntaje += 2
    return puntaje

def determinar_nivel(puntaje):
    if puntaje <= 4:
        return NIVELES[0]
    elif puntaje <= 7:
        return NIVELES[1]
    else:
        return NIVELES[2]

def procesar_contraseña(contraseña, generada=False):
    puntaje = evaluar_contraseña(contraseña)
    nivel = determinar_nivel(puntaje)
    if generada:
        print("\nContraseña generada:", contraseña)
    print("Nivel alcanzado:", nivel)
    print("Puntaje obtenido:", puntaje)

    # Guardar información completa en el historial
    historial.append({
        "usuario": usuario_actual,
        "contraseña": contraseña,
        "puntaje": puntaje,
        "nivel": nivel
    })

def mostrar_historial():
    if not historial:
        print("No hay contraseñas registradas aún.")
    else:
        print("\n--- Historial de Contraseñas Evaluadas ---")
        for i, entrada in enumerate(historial, 1):
            print(f"{i}. Usuario: {entrada['usuario']} | Contraseña: {entrada['contraseña']} | Puntaje: {entrada['puntaje']} | Nivel: {entrada['nivel']}")

# INICIO DEL PROGRAMA
print("Bienvenido al Juego Generador de Contraseñas Seguras")
obtener_nombre_usuario()

while True:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue

    if opcion == 5:
        break
    elif opcion == 1:
        mostrar_reglas()
    elif opcion == 2:
        contraseña = generar_contraseña()
        procesar_contraseña(contraseña, generada=True)
    elif opcion == 3:
        intentos_realizados = 0
        while intentos_realizados < MAX_INTENTOS:
            contraseña = input(f"Ingrese su contraseña ({intentos_realizados + 1}/{MAX_INTENTOS}): ")
            procesar_contraseña(contraseña)
            intentos_realizados += 1
        print("Has usado todos los intentos. Regresando al menú principal...")
    elif opcion == 4:
        mostrar_historial()
    else:
        print("Opción no válida. Intente nuevamente.")

print(f"Gracias por jugar, {usuario_actual}. ¡Hasta pronto!")
