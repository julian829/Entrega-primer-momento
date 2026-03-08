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

def main():
    print("Astrologic")
    print("Entrega Python 1")
    menu()

main()