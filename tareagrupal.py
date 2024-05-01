import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('coches_de_segunda_mano.csv', sep=',', encoding='utf-8')

# Porcentaje de registros por país
porcentaje_registros_por_pais = (df['country'].value_counts() / len(df)) * 100

# Gráfico de Porcentaje de registros por país
plt.figure(figsize=(10, 6))
porcentaje_registros_por_pais.plot(kind='bar', color='orange')
plt.title('Porcentaje de registros por país')
plt.ylabel('Porcentaje')
plt.xlabel('País')
plt.xticks(rotation=45)
plt.show()

# Porcentaje de registros por año
porcentaje_registros_por_anio = (df['year'].value_counts() / len(df)) * 100

# Gráfico de Porcentaje de registros por año
plt.figure(figsize=(10, 6))
porcentaje_registros_por_anio.plot(kind='bar', color='green')
plt.title('Porcentaje de registros por año')
plt.ylabel('Porcentaje')
plt.xlabel('Año')
plt.xticks(rotation=45)
plt.show()

# Porcentaje de registros por tipo de combustible
porcentaje_registros_por_combustible = (df['fuel'].value_counts() / len(df)) * 100

# Gráfico de Porcentaje de registros por tipo de combustible
plt.figure(figsize=(10, 6))
porcentaje_registros_por_combustible.plot(kind='bar', color='blue')
plt.title('Porcentaje de registros por tipo de combustible')
plt.ylabel('Porcentaje')
plt.xlabel('Tipo de Combustible')
plt.xticks(rotation=45)
plt.show()

# Porcentaje de registros por provincia
porcentaje_registros_por_provincia = (df['province'].value_counts() / len(df)) * 100

# Gráfico de Porcentaje de registros por provincia
plt.figure(figsize=(12, 6))
porcentaje_registros_por_provincia.plot(kind='bar', color='purple')
plt.title('Porcentaje de registros por provincia')
plt.ylabel('Porcentaje')
plt.xlabel('Provincia')
plt.xticks(rotation=45)
plt.show()

# Porcentaje de registros por marca de coche
porcentaje_registros_por_marca = (df['make'].value_counts() / len(df)) * 100

# Gráfico de Porcentaje de registros por marca de coche
plt.figure(figsize=(12, 6))
porcentaje_registros_por_marca.plot(kind='bar', color='pink')
plt.title('Porcentaje de registros por marca de coche')
plt.ylabel('Porcentaje')
plt.xlabel('Marca')
plt.xticks(rotation=45)
plt.show()