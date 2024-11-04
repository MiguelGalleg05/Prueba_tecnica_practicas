
import pandas as pd #  Se importa  la librería pandas, que ayuda con el manejo de dataframe

file_path = 'data/Prueba_Tecnica_Practicante.xlsx'
df_casos = pd.read_excel(file_path, sheet_name="Casos") # Aca se carga el archivo de Excel con la pestaña "Casos"

df_casos_bd = df_casos.melt(id_vars=["Red", "Tipo"], var_name="Fecha", value_name="Cant_Casos") # Aca se hace la tranformacion solicitada

df_casos_bd['Fecha'] = pd.to_datetime(df_casos_bd['Fecha']).dt.strftime('%d/%m/%Y') #  Aca se convierte la columna 'Fecha' al formato (DD/MM/YYYY)

df_casos_bd['Red'] = df_casos_bd['Red'].ffill() # Rellena los Nan en Red para que quede el nombre de la Red , en la fila de Registro Publica y Privada

df_casos_bd.to_excel('outputs/df_casos_bd.xlsx', index=False)# Aca se Exportar el DataFrame transformado a un archivo de Excel
print("Archivo 'df_casos_bd.xlsx' generado con éxito..") 

