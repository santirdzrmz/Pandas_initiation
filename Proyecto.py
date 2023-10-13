import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
import csv


def csvReader():
    archivo = []
    with open('summer-products.csv', newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            archivo.append(fila)
    return archivo

def df():
    dataframe = pd.read_csv("summer-products.csv")
    return dataframe

def addBoost(archivo):
    print('¿Qué quieres saber?')
    print('1. Cuantas prendas sí tuvieron add boost.')
    print('2. Cuántas prendas no tuvieron add boost.')
    x= int(input())

    contador0 = 0
    contador1 = 0
    # contar 0 y 1s en col 7 (tiene add boost)
    for i in range(1, len(archivo)): 
        if len(archivo[i]) > 6:
            valor = float(archivo[i][6]) 
            if valor == 0.0:
                contador0 += 1
            elif valor == 1.0:
                contador1 += 1
            else:
                print("No tiene valores suficientes")
    
    if x==1:
        print('De las', (contador0+contador1), 'prendas,', contador1, 'tuvieron ad boost.')
        print('La gráfica de los porcentajes se mostrará a continuación')
    else:
        print('De las', (contador0+contador1), 'prendas,', contador0, 'no tuvieron ad boost.')
        print('La gráfica de los porcentajes se mostrará a continuación')
    
    valores_grafica= [contador0, contador1]
    labels= ['Sin add boost','Con add boost']

    mp.pie(valores_grafica, labels=labels, autopct='%1.1f%%')
    mp.title('Add boosts')
    mp.show()
    
def topNumbers(df):
    print("Escoge el menor valor del dinero:")
    min = int(input())
    print("Escoge el mayor valor del dinero:")
    max = int(input())
    print("Escoge el numero de valores que quieres mostrar: ")
    valor = int(input())
    i = 0
    data = []
    while i < df.shape[0]:
        precio = float(df.loc[i, "retail_price"])
        if precio <= max and precio >= min:
                row = df.iloc[i]
                data.append(row)
        i += 1
    especifico_df = pd.DataFrame(data)
    sorteado_df = especifico_df.sort_values(by=["units_sold"], ascending=False)
    lista = sorteado_df.head(valor).reset_index(drop=True)
    nombres = []
    unidades = []
    filas = 0
    while filas < lista.shape[0]:
            nombre = lista.loc[filas, "title"]
            nombre_deconstruido = nombre.split()
            resultante = nombre_deconstruido[0]+" "+nombre_deconstruido[1]
            nombres.append(resultante)
            unidades.append(lista.loc[filas, "units_sold"])
            filas+=1
    n=0
    print("Las prendas mas vendidas son: ")
    while n < len(nombres):
        print(nombres[n]+" N. de unidades: "+str(unidades[n]))
        n+=1
    mp.bar(nombres,unidades)
    mp.show()
    

def percentageCalculator(dataframe):
    check = False
    min = None
    max = None
    while check == False:
        try:
            print("Escoge el valor minimo de dinero:")
            min = int(input())
            print("Escoge el valor maximo de dinero")
            max = int(input())
            check = True
        except:
            print("Escoge un numero entero!\n")
    five = 0
    four = 0
    three = 0
    two = 0
    one = 0
    zero=0
    count = 0
    data = []
    while count < dataframe.shape[0]:
        number = float(dataframe.loc[count, "retail_price"])
        if number <= max and number >= min:
                row = dataframe.iloc[count]
                data.append(row)
        count += 1
    specific_dataframe = pd.DataFrame(data)
    count = 0
    while count < dataframe.shape[0]:
        try:
            if float(specific_dataframe.loc[count, "rating"]) < 1:
                zero+=1
                count+=1
            elif float(specific_dataframe.loc[count, "rating"]) >= 1 and float(specific_dataframe.loc[count, "rating"]) < 2:
                one+=1
                count+=1
            elif float(specific_dataframe.loc[count, "rating"]) >= 2 and float(specific_dataframe.loc[count, "rating"]) < 3:
                two+=1
                count+=1
            elif float(specific_dataframe.loc[count, "rating"]) >= 3 and float(specific_dataframe.loc[count, "rating"]) < 4:
                three+=1
                count+=1
            elif float(specific_dataframe.loc[count, "rating"]) >= 4 and float(specific_dataframe.loc[count, "rating"]) < 5:
                four+=1
                count+=1
            else:
                five+=1
                count+=1
        except:
            count+=1

    print("Numero de 5 estrellas en el rango: "+str(five))
    print("Numero de 4-4.99 estrellas en el rango: "+str(four))
    print("Numero de 3-3.99 estrellas en el rango: "+str(three))
    print("Numero de 2-2.99 estrellas en el rango: "+str(two))
    print("Numero de 1-1.99 estrellas en el rango: "+str(one))
    print("Numero de 0-0.99 estrellas en el rango: "+str(zero))
    final_array= np.array([five, four, three, two, one, zero])
    return final_array

def printGraph(array):
    these_labels=["5 rating", "4.99-4 rating", "3.99-3 rating", "2.99-2 rating", "1.99-1 rating", "0.99-0 rating"]
    mp.pie(array, labels = these_labels)
    mp.legend()
    mp.show()


def main():
    print("Hola! Bienvenido a el analizador de prendas. ")
    print("--------------------------------------------")
    print("Que opcion quieres escoger? Selecciona el numero: ")
    check = False
    while check == False:
        print("1. Estadística de la relación entre add boost y cantidad de ventas. (Pie graph)")
        print("2. Estadística que demuestre un número especifico de las unidades más vendidas dentro de un rango especifico de dinero. (Bar graph)")
        print("3. Estadística que enseña el porcentaje de reseñas de 5, 4, 3, 2, y 1 estrellas dentro de un rango específico de dinero. (Pie graph)")
        try:
            entry = int(input())
            if entry > 0 and entry<4: 
                check = True
        except:
            print("Escoga un numero entero\n")
    if entry == 1:
        archivo = csvReader()
        addBoost(archivo)
    elif entry == 2:
        dataframe = df()
        topNumbers(dataframe)
    else:
        dataframe = df()
        array = percentageCalculator(dataframe)
        printGraph(array)
    
main()