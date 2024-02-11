'''
Requerimientos del desarrollo del software

°   R1- The program shall be invoked from a
command line. The program shall receive two
files as parameters. The first file will contain
information in a JSON format about a catalogue
of prices of products. The second file will
contain a record for all sales in a company.

°   R2-  The program shall compute the total cost
for all sales included in the second JSON archive.
The results shall be print on a screen and on a
file named SalesResults.txt. The total cost
should include all items in the sale considering
the cost for every item in the first file.

°   R3- The program shall include the mechanism
to handle invalid data in the file. Errors should
be displayed in the console and the execution
must continue.

°   R4- The name of the program shall be
computeSales.py

°   R5-  The minimum format to invoke the
program shall be as follows:
python computeSales.py priceCatalogue.json
salesRecord.json

°   R6- The program shall manage files having
from hundreds of items to thousands of items.

°   R7- The program should include at the end of
the execution the time elapsed for the
execution and calculus of the data. This number
shall be included in the results file and on the
screen.

°   R8-  Be compliant with PEP8.

'''
import sys
import pandas as pd
import time


def main():
    # Verifica que se proporcionen dos argumentos
    if len(sys.argv) != 3:
        print("Usage: python program.py <prices_file.json> <sales_file.json>")
        return

    # Lee los nombres de los archivos desde los argumentos
    # de la línea de comandos
    prices_file = sys.argv[1]
    sales_file = sys.argv[2]

    # Intenta leer los archivos JSON
    try:
        prices_df = pd.read_json(prices_file)
        sales_df = pd.read_json(sales_file)
        Tiempo_inicial = time.time()
    except FileNotFoundError:
        print("Error: One or both files not found.")
        return
    except ValueError:
        print("Error: One or both files are not valid JSON.")
        return

    # Creamos un data frame en donde se relaciones ambos registros
    prices_df = prices_df.rename(columns={'title': 'Product'})
    Merge_df = pd.merge(prices_df, sales_df, on='Product')

    # Calculo del costo total
    Merge_df['Costos'] = (Merge_df['Quantity'] * Merge_df['price'])
    Costo_total = Merge_df["Costos"].sum()

    # Calculo del tiempo de ejecucion
    Tiempo_final = time.time()
    Tiempo_ejecución = (Tiempo_final - Tiempo_inicial) * 1000

    # Desplegamos toda la información solicitada
    print("\nCosto total: ", Costo_total)
    print("\nTiempo de ejecucion: " + str(Tiempo_ejecución) + ' milisegundos')

    # Creamos el archivo txt con los resultados
    with open('SalesResults.txt', 'w') as file:
        file.write("Costo total: {}\n".format(Costo_total))
        file.write("Tiempo de ejecucion: {} milisegundos\n"
                   .format(Tiempo_ejecución))


if __name__ == "__main__":
    main()
