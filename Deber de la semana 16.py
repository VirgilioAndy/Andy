# Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    file.write("Estas son mis notas personales:\n")
    file.write("1. Hacer ejercicio por la mañana.\n")
    file.write("2. Comprar leche y huevos en el supermercado.\n")
    file.write("3. Tomar tiempo para relajarse y leer un libro antes de dormir.\n")

# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    print("Contenido del archivo my_notes.txt:")
    for line in file:
        print(line.strip())