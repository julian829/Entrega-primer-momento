eventos = []

def menu():
    print("\n=== ASTROLOGIC ===")
    print("1. Registrar evento")
    print("2. Ver eventos")
    print("3. Salir")

def registrar_evento():
    nombre = input("Ingrese el nombre del evento: ")
    fecha = input("Ingrese la fecha del evento: ")

    evento = {
        "nombre": nombre,
        "fecha": fecha
    }

    eventos.append(evento)
    print("Evento registrado correctamente")

def ver_eventos():
    if len(eventos) == 0:
        print("No hay eventos registrados")
    else:
        print("\nEventos registrados:")
        for i, evento in enumerate(eventos, start=1):
            print(f"{i}. Nombre: {evento['nombre']} - Fecha: {evento['fecha']}")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_evento()
        elif opcion == "2":
            ver_eventos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")

main()