import pandas as pd

ruta_archivo = 'C:/Users/diego/Desktop/archive/Online_Retail.csv'

# Cargar el archivo CSV como un DataFrame con la codificación correcta
df = pd.read_csv('C:/Users/diego/Desktop/archive/Online_Retail.csv'
, encoding='latin1')  # o 'ISO-8859-1', dependiendo de la codificación del archivo


# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('C:/Users/diego/Desktop/archive/Online_Retail.csv'
, index=False)

#Agrupar datos por país
grouped = df.groupby('Country').sum()
print(grouped)

#Definir disponibilidad de productos en stock por país
def in_stock(row):
    if row['Quantity'] > 0:
        return 'In stock'
    else:
        return 'Out of stock'
df['Stock'] = df.apply(in_stock, axis=1)
print(df['Stock'])


#Extraer ventas totales por país
df['Total'] = df['Quantity'] * df['UnitPrice']
total_sales = df.groupby('Country').sum()
print(total_sales)

#Filtrado de datos
df_filtered = df[df['Country'] == 'United Kingdom']
print(df_filtered)

#Ordenar ventas por pais
df_sorted = df.sort_values(by='Country', ascending=False)
print(df_sorted)

#Ventas más altas del Reino Unido
uk_sales = df[df['Country'] == 'United Kingdom']
uk_sales = uk_sales.groupby('Description').sum()
uk_sales = uk_sales.sort_values(by='Quantity', ascending=False)
print(uk_sales)

#Extraer ventas en 2010
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Year'] = df['InvoiceDate'].dt.year
df_2010 = df[df['Year'] == 2010]
print(df_2010)

#pivot tables

pivot = df.pivot_table(index='Country', columns='Year', values='Total', aggfunc='sum')
print(pivot)

#ordenar información por orden alfabético
df = df.sort_values(by='Country')
print(df)

#Fusionar dataframes
df1 = df[df['Country'] == 'United Kingdom']
df2 = df[df['Country'] == 'France']
df3 = pd.concat([df1, df2])
print(df3)

#Uso de join
df1 = df[df['Country'] == 'United Kingdom']
df2 = df[df['Country'] == 'France']
df3 = df1.join(df2, lsuffix='_UK', rsuffix='_FR')
print(df3)