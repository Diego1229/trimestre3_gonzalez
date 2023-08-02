import csv
ruta_completa = "C:\\trab\\trimestre3_gonzalez\\csv\\nombres.csv"
with open('nombres.csv') as f:
   reader = csv.reader(f)
   for row in reader:
        print("nombre: {0}, edad: {1}".format(row[0], row[1]))
