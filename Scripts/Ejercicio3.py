import pandas as pd # Se importa pandas para el manejo de dataframes
import sqlite3 # se importa esta libreria para trabajar la base de datos  

conn = sqlite3.connect(':memory:') # se crea una bd sqlite en memoria  o sea temporal 


file_path = 'Outputs/df_casos_union.xlsx' # Ruta del archivo que tiene los datos
df_casos_union = pd.read_excel(file_path) # Se carga el excel en un dataframe de pandas

df_casos_union['Fecha'] = pd.to_datetime(df_casos_union['Fecha'], format='%d/%m/%Y') # Se convierte la columna fecha  a otro formato


df_casos_union.to_sql('df_casos_union', conn, index=False, if_exists='replace') # se guarda el dataframe en la bd

# se define la consulta  para agrupar y sumar 
query = """ 
SELECT
    Red,
    Tipo,
    strftime('%Y', Fecha) AS Año,
    strftime('%m', Fecha) AS Mes,
    SUM(Cant_Casos) AS Cant_Casos
FROM
    df_casos_union
GROUP BY
    Red, Tipo, strftime('%Y', Fecha), strftime('%m', Fecha);
"""


result = pd.read_sql_query(query, conn) # Ejecuta la consulta


result.to_excel('outputs/resultado_casos.xlsx', index=False) # Exporta el archivo excel 
print("Archivo 'resultado_casos.xlsx' generado con éxito.") # Mensaje de que todo bien 

with open('Querys/consulta.sql', 'w') as file: # abre o crea el archivo para guardar la consulta
    file.write(query)

print("¡Consulta ejecutada y archivos generados exitosamente!") # Mensaje de que todo bien
