# crear función para crear columnas flags
# Importamos el dataset

# Importar librería y leer datos
import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

def crear_flags(df, flags_cols):
    for col in flags_cols:
        nombre_flag = col + "_missing_flag" # nombre de la nueva columna flag
        df[nombre_flag] = df[col].isna().astype(int) # crea la columna flag con 1 si es nulo, 0 si no lo es
    return df

# establecer columnas a procesar
columnas_flags= ["customer_age", "city", "state"]

# aplicar función y mostrar resultados
df = crear_flags_antes_de_imputar(df, columnas_flags) # aplica la función para crear las columnas flags
df.info()
print(df.head())