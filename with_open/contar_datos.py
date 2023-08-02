def contar_caracteres_y_lineas():
    archivo = open("datos.txt", "r")
    datos_texto = archivo.read()
    archivo.close()

    num_caracteres = len(datos_texto)
    num_lineas = datos_texto.count("\n") + 1

    return num_caracteres, num_lineas

caracteres, lineas = contar_caracteres_y_lineas()

print(f"Número de caracteres en el archivo: {caracteres}")
print(f"Número de líneas en el archivo: {lineas}")
