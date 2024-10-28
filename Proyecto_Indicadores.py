import pandas as pd


# Creo los dataframes
data_paises = pd.read_excel(r"C:\Users\kbm19\Desktop\Franco Cursos\Proyectos\Proyectos Indicadores Mundiales\Paises.xlsx")
data_poblacion = pd.read_excel(r"C:\Users\kbm19\Desktop\Franco Cursos\Proyectos\Proyectos Indicadores Mundiales\Population.xlsx")
data_Expectativa = pd.read_excel(r"C:\Users\kbm19\Desktop\Franco Cursos\Proyectos\Proyectos Indicadores Mundiales\Life+expectancy.xlsx")
data_mortalidad = pd.read_excel(r"C:\Users\kbm19\Desktop\Franco Cursos\Proyectos\Proyectos Indicadores Mundiales\Infant+death+rate.xlsx")
data_country = pd.read_excel(r"C:\Users\kbm19\Desktop\Franco Cursos\Proyectos\Proyectos Indicadores Mundiales\Countries.xlsx")

# --- Exploracion Inicial de datos ---
# 1) Paises

print("\nPrimeras filas Tabla Paises")
print(data_paises.head())

print("\nTamaño de la Tabla Paises")
print(data_paises.shape)

print("\nInformacion de la Tabla Paises")
print(data_paises.info())

print("\nValores nulos en la tabla:")
print(data_paises.isnull().sum())

# 2) Poblacion 

print("\nPrimeras filas Tabla Poblacion")
print(data_poblacion.head())

print("\nTamaño de la Tabla Poblacion")
print(data_poblacion.shape)

print("\nInformacion de la Tabla Poblacion")
print(data_poblacion.info())

print("\nValores nulos en la tabla:")
print(data_poblacion.isnull().sum())

# 3) Expectativa de vida 

print("\nPrimeras filas Tabla Expectativa")
print(data_Expectativa.head())

print("\nTamaño de la Tabla expectativa")
print(data_Expectativa.shape)

print("\nInformacion de la Tabla Expectativa")
print(data_Expectativa.info())

print("\nValores nulos en la tabla:")
print(data_Expectativa.isnull().sum())

# 4) Mortalidad

print("\nPrimeras filas Tabla mortalidad")
print(data_mortalidad.head())

print("\nTamaño de la Tabla Mortalidad")
print(data_mortalidad.shape)

print("\nInformacion de la Tabla Mortalidad")
print(data_mortalidad.info())

print("\nValores nulos en la tabla:")
print(data_mortalidad.isnull().sum())

# 5) Country

print("\nPrimeras filas Tabla Country")
print(data_country.head())

print("\nTamaño de la Tabla country")
print(data_country.shape)

print("\nInformacion de la Tabla Country")
print(data_country.info())

print("\nValores nulos en la tabla:")
print(data_country.isnull().sum())