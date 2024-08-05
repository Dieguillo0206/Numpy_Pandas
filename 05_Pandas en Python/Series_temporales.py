import pandas as pd

ruta_archivo = 'C:/Users/diego/Desktop/archive/Online_Retail.csv'

# Cargar el archivo CSV como un DataFrame con la codificación correcta
df = pd.read_csv('C:/Users/diego/Desktop/archive/Online_Retail.csv'
                 , encoding='latin1')  # o 'ISO-8859-1', dependiendo de la codificación del archivo


# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('C:/Users/diego/Desktop/archive/Online_Retail.csv'
          , index=False)

#Convertir la columna 'InvoiceDate' a tipo datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
#formato invoiceDate
print(df['InvoiceDate'].dt.strftime('%d-%m-%Y %H:%M:%S'))

#Extraer ventas mensuales
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('Month').sum()
print(monthly_sales)