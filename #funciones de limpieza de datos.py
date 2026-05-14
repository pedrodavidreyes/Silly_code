#funciones de limpieza de datos

#una sola función + un loop
#En lugar de escribir una función por columna, podemos escribir una única función que recibe una lista de columnas y usa un loop interno para aplicar la misma regla a cada una.
#Esto elimina completamente la repetición de código y hace la limpieza escalable.

import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

# Creamos una función que convierte a numérico varias columnas a la vez, usando un loop interno para iterar sobre 
# la lista de columnas.
def convertir_columnas_numericas(df, columnas):
    for col in columnas:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

# Creamos una lista con las columnas que queremos convertir a numérico
columnas_numericas = ["price", "quantity", "order_value"]

# Llamamos a la función pasando el DataFrame y la lista de columnas
df = convertir_columnas_numericas(df, columnas_numericas)
df.info()

#Escalabilidad: cambiar la lista cambia el resultado sin reescribir código.