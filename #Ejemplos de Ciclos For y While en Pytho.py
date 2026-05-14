#Ejemplos de Ciclos For y While en Python - Automatización de limpieza:

# ejemplo de ciclo for para revisar nulos en varias columnas
import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")
# De esta forma se puede revisar cada columna por separado, pero es un poco repetitivo
print("product_category nulos:", df["product_category"].isna().sum())
print("quantity nulos:", df["quantity"].isna().sum())
print("city nulos:", df["city"].isna().sum())
# Para evitar la repetición, se puede usar un ciclo for para revisar varias columnas a la vez
columnas = ["product_category", "quantity", "city"] #se crea una lista con los nombres de las columnas a revisar
# Luego se recorre la lista con un ciclo for, y se imprime el nombre de la columna y la cantidad de nulos que tiene
for col in columnas:
    print(col, "nulos:", df[col].isna().sum())

# Ejemplo de ciclo for para buscar centinelas (sentinels)
import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")
columnas = ["customer_age", "quantity", "order_value"]
sentinel = -999
for col in columnas:
    print(col,"→", df[col].isin([-999]).sum())

#Limpieza de bloques completos con ciclos for
#Un analista rara vez limpia solo una columna. Normalmente limpia bloques completos:
columnas_texto = ["city", "state", "product_category"]
for col in columnas_texto:
    df[col] = df[col].str.strip().str.lower()


# Sin embargo cuando:
# no sabes cuántas repeticiones habrá,
# repites hasta que se cumpla una condición
# Entonces es mejor usar ciclos while
# 💡 En limpieza y análisis de datos, usamos más el for porque es más seguro y predecible. 
# Dejamos while para casos específicos, siempre revisando que el bucle termine.

# Ejemplo de ciclo while para revisar ventas
ventas = 993
#completa el código dentro del while
while ventas <= 1000:
    print("Ventas registradas:", ventas)
    ventas=ventas+1