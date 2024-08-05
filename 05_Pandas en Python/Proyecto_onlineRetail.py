import pandas as pd

ruta_archivo = 'C:/Users/diego/Desktop/archive/Online_Retail.csv'

# Especificar los tipos de datos para cada columna (ajusta según tu archivo)
dtype = {
    'InvoiceNo': 'str',
    'StockCode': 'str',
    'Description': 'str',
    'Quantity': 'int',
    'InvoiceDate': 'str',
    'UnitPrice': 'float',
    'CustomerID': 'str',
    'Country': 'str'
}

# Leer el archivo CSV en partes más pequeñas
chunksize = 100000  # Ajusta el tamaño del chunk según sea necesario

# Crear un DataFrame vacío para concatenar los chunks
df_list = []

for chunk in pd.read_csv(ruta_archivo, encoding='latin1', dtype=dtype, chunksize=chunksize):
    df_list.append(chunk)

# Concatenar todos los chunks en un solo DataFrame
df = pd.concat(df_list, ignore_index=True)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('C:/Users/diego/Desktop/archive/Online_Retail_modificado.csv', index=False)

print(df)

