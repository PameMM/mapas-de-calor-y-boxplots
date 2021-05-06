# Importamos las librerías necesarias
import csv

# Declaramos las variables de cantidad y las iniciamos en 0
NumeroHombres = 0
NumeroMujeres = 0

# Abrimos el archivo de excel
with open('insurance.csv', newline='') as csvfile:
    # Abrirlo en modo lectura
    reader = csv.DictReader(csvfile)
    
    # Por cada fila en el archivo...
    for row in reader:
        if row['sex'] == 'female': # Si 'sex' == 'female'
            NumeroMujeres += 1 # Sumamos 1 en NumeroMujeres
        elif row['sex'] == 'male': # Si 'sex' == 'male'
            NumeroHombres += 1 # Sumamos 1 en NumeroHombres

# Imprimimos los resultados
print("Numero de Hombres: ",NumeroHombres)
print("Numero de Mujeres: ",NumeroMujeres)