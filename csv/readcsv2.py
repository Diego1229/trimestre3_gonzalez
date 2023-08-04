from paises import *
import csv
listaPaises=[]
with open("pais.csv","r") as csvDataFile:
    
    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        ob=paises(row[1],row[4],row[3],row[11])
        listaPaises.append(ob)
       
for apr in listaPaises:
    print('el nombre del pais :',apr.getNombre())
    print('la superficie del pais es:',apr.Superficie())
    print('la altura del pais es: ',apr.getAltura())
    print('el nominal del pais es:',apr.getNominal())



