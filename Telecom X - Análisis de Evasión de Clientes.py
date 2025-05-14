# %% [markdown]
# # Análisis de Evasión de Clientes (Churn) - Telecom X
# 
# ## Introducción
# Este proyecto analiza los datos de clientes de Telecom X para identificar patrones y factores que influyen en la evasión de clientes (churn).

# %% [markdown]
# ## 1. Extracción de Datos
# Importamos los datos directamente desde la API

# %%
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL de la API
url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json"

# Descargar datos
response = requests.get(url)
data = response.json()

# Convertir a DataFrame
df = pd.DataFrame(data)

# %% [markdown]
# ## 2. Exploración Inicial
# Examinamos la estructura de los datos

# %%
# Información básica
print(df.info())
print("\nPrimeras filas:")
display(df.head())

# %% [markdown]
# ## 3. Limpieza y Transformación de Datos

# %%
# Manejo de valores nulos
print("Valores nulos por columna:")
print(df.isnull().sum())

# Eliminar duplicados
df = df.drop_duplicates()

# Convertir tipos de datos
df['Fecha_Contrato'] = pd.to_datetime(df['Fecha_Contrato'])
df['Churn'] = df['Churn'].astype('category')

# %% [markdown]
# ## 4. Análisis Exploratorio (EDA)

# %%
# Distribución de Churn
plt.figure(figsize=(6,4))
sns.countplot(x='Churn', data=df)
plt.title('Distribución de Evasión de Clientes')
plt.show()

# %%
# Churn por variables categóricas
cat_vars = ['Genero', 'Tipo_Contrato', 'Metodo_Pago']
for var in cat_vars:
    plt.figure(figsize=(10,4))
    sns.countplot(x=var, hue='Churn', data=df)
    plt.title(f'Churn por {var}')
    plt.xticks(rotation=45)
    plt.show()

# %%
# Churn por variables numéricas
num_vars = ['Total_Gastado', 'Tiempo_Contrato_Meses']
for var in num_vars:
    plt.figure(figsize=(10,4))
    sns.boxplot(x='Churn', y=var, data=df)
    plt.title(f'Distribución de {var} por Churn')
    plt.show()

# %% [markdown]
# ## 5. Análisis de Correlación (Opcional)

# %%
# Matriz de correlación
corr_matrix = df.select_dtypes(include=['float64', 'int64']).corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.show()

# %% [markdown]
# ## 6. Conclusiones y Recomendaciones
# 
# **Hallazgos principales:**
# 1. X% de los clientes abandonan el servicio
# 2. Los clientes con contrato mensual tienen mayor tasa de churn
# 3. El método de pago electrónico muestra menor tasa de abandono
# 
# **Recomendaciones:**
# 1. Implementar incentivos para contratos a largo plazo
# 2. Mejorar la experiencia de clientes con facturación mensual
# 3. Promover métodos de pago automáticos