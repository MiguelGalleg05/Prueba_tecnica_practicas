import pandas as pd #  Importa la librería pandas, que ayuda con el manejo de dataframe

file_path = 'data/Prueba_Tecnica_Practicante.xlsx'
df_casos_bd = pd.read_excel('outputs/df_casos_bd.xlsx')
df_meta = pd.read_excel(file_path, sheet_name='Meta')  # Aca se carga el archivo de Excel con la pestaña "Meta"



df_casos_union = pd.merge(df_casos_bd, df_meta, on=["Red", "Tipo"], how="left") # Aca se realiza la unión entre df_casos_bd y df_meta en las columnas "Red" y "Tipo"


df_casos_union['% Cumplimiento'] = (df_casos_union['Cant_Casos'] / df_casos_union['Meta']) #Aca se calcula el % de cumplimiento

output_file = 'outputs/df_casos_union.xlsx' # Aca se define la ruta de salida del Archivo 
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer: # Aca se abre el escritor , que es una herramiento que ayuda a escribir en archivos xls
    df_casos_union.to_excel(writer, index=False, sheet_name='Cumplimiento') # Aca se exporta excel unido a una nueva hoja 

    workbook = writer.book
    worksheet = writer.sheets['Cumplimiento'] # Aca se obtiene el libro de trabajo y selecciona donde se guardo la hoja 

    percent_format = workbook.add_format({'num_format': '0%'}) # Aca se establece el formato %
    
    worksheet.set_column('F:F', None, percent_format)  # Aca se establece el formato creado antes, a la columna cumplimiento para que se muestre en %

print("Archivo 'df_casos_union.xlsx' generado con éxito.") # Aca ya un mensaje de exito si todo salio full
 