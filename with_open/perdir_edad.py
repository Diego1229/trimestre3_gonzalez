def solicitar_datos():
    edad = input("¿Qué edad tienes?: ")
    nombre = input("¿Cuál es tu nombre?: ")
    altura = input("¿Cuál es tu altura?: ")

    archivo = open("datos.txt", "w")
    archivo.write(f"Nombre: {nombre}\nEdad: {edad}\nAltura: {altura}")
    archivo.close()

    print("Datos guardados exitosamente.")

solicitar_datos()  # Llamada directa a la función




         