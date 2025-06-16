import random 
import string

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Ver Reglas del Juego")
    print("2. Generar Contraseña Automáticamente")
    print("3. Crear Contraseña Manualmente")
    print("4. Salir")

def mostrar_reglas():
    print("\n--- Reglas del Juego ---")
    print("Tu objetivo es generar contraseñas seguras.")
    print("Puedes dejar que el sistema la genere o escribir una tú mismo.")
    print("La contraseña será evaluada y clasificada por seguridad.")
    print("¡Mientras más fuerte, más puntos obtienes!")

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

def determinar_nivel(contraseña):
    puntaje = evaluar_contraseña(contraseña)
    if puntaje <= 4:
        return "Débil"
    elif puntaje <= 7:
        return "Media"
    else:
        return "Fuerte"

# Inicio del Programa
print("Bienvenido al Juego Generador de Contraseñas Seguras")

while True:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción (1-4): "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue

    if opcion == 4:
        break
    elif opcion == 1:
        mostrar_reglas()
    elif opcion == 2:
        contraseña = generar_contraseña()
        puntaje = evaluar_contraseña(contraseña)
        nivel = determinar_nivel(contraseña)
        print("\nContraseña generada:", contraseña)
        print("Nivel alcanzado:", nivel)
        print("Puntaje obtenido:", puntaje)
    elif opcion == 3:
        contraseña = input("Ingrese su contraseña: ")
        puntaje = evaluar_contraseña(contraseña)
        nivel = determinar_nivel(contraseña)
        print("Nivel alcanzado:", nivel)
        print("Puntaje obtenido:", puntaje)
    else:
        print("Opción no válida. Intente nuevamente.")

print("Gracias por jugar.")