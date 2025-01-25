
#Tarea 3 Probabilidad y estadistica
#Importacion de libreriasd y Dataset

#Con estos codigos puedo agregar un archivo para poder visualizarlo y ejecutarlo
import pandas as pd
data = pd.read_csv('SoftwareProject_DataSet.csv')

#Verificacion del contenido del DataSet
data.head()

#Identificar poblaciones y muestras
#Obtener el tamaño de la poblacion: Con estas lineas de codigo puedo saber el tamaño total de la poblacion
population_size = len(data)
print("Tamaño de la poblacion:", population_size)

##Creacion de una muestra aleatoria simple de 50 registros: con este codigo puedo hacer que al ejecutarlo agarre datos aleatoriamente.
sample_size = 50
sample = data.sample(n=sample_size, random_state=42)
display(sample)

#Descripcion estadistica de la poblacion completa: Con este codigo podemos obtener una descripcion estadistica de lo anterior (Poblacion Total)
population_desc = data[['Costo (USD)', 'Tiempo de desarrollo (horas)']].describe()
print("Descripcion de la poblacion completa:")
display(population_desc)

###Muestreo Aleatorio sistematico
##Seleccion sistema de una muestra
#Definicion del intervalo K (Tamaño poblacional / muestra deseada): con este codigo podemos seleccionar una muestra sistematica
sample_size = 50
interval = population_size // sample_size

#seleccion de muestra sistematica
systematic_sample = data.iloc[::interval]

#Verificar la muestra
print("Muestra obtenida por muestreo sistematico:")
display(systematic_sample)

###Analisis de Subpoblaciones
#Dividir la poblacion por tipo de proyecto
grouped_by_project_type = data.groupby('Tipo de proyecto')

#Calcular el promedio de lineas de codigo y bugs para cada tipo
group_analysis = grouped_by_project_type[['Líneas de código', 'Número de bugs']].mean()
print("Analisis por tipo de proyecto:")
display(group_analysis)

#Crear una muestra estratificada por 'Tipo de proyecto'
stratifed_sample = grouped_by_project_type.sample(n=15, random_state=42)

print("Muestra estatificada por tipo de proyecto:")
display(stratifed_sample)

##comparacion entre Muestra y Poblacion
#Descripcion Estadistica de la muestra aleatoria simple: con este codigo podemos obtener otra descripcion de la muestra aleatoria
sample_description = sample[['Costo (USD)', 'Tiempo de desarrollo (horas)']].describe()
print("Descripcion de la muestra aleatoria simple:")
display ( sample_description)

#Descripcion Estadistica de la poblacion
data_description = data[['Costo (USD)', 'Tiempo de desarrollo (horas)']].describe()
print("Descripcion de la poblacion completa:")
display(data_description)

##Comparacion de Metodos de Muestreo
#Muestreo por conglomerados basicos en "Fase del proyecto"
grouped_by_phase = data.groupby('Fase del proyecto')
conglomerate_sample = grouped_by_phase.sample(n=10, random_state=42)
display(conglomerate_sample)

#Muestreo de conveniencia: Seleccion de las primeras 50 filas
convenience_sample = data.head(50)

print("Muestra de conveniencia")
display(convenience_sample)


###Habian varios codigos los cuales no habia visto como por ejemplo pd.DataFrame que por alguna razon lo probre y siempre me daba error, no supe como sonucionarlo y mejor lo quite del codigo ya que no me corria el codigo como debia.




