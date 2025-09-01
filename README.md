# 📊 Contact Center Analytics – Python, SQL & Power BI
Este proyecto corresponde a una **prueba técnica de analítica**, enfocada en el manejo de datos de un **Contact Center en redes sociales**.  
Se trabajaron transformaciones con **Python (Pandas)**, consultas en **SQL (SQLite)** y visualización en **Power BI**.

## 🚀 Ejercicios desarrollados

### 🔹 Ejercicio 1 – Transformación inicial
- Lectura de la pestaña **Casos** del archivo Excel.
- Conversión a DataFrame `df_casos_bd` con la estructura:
Red | Tipo | Fecha | Cant_Casos

- Exportación del resultado a `df_casos_bd.xlsx`.  
📂 Script: [`Ejercicio1.py`](Ejercicio1.py)

### 🔹 Ejercicio 2 – Unión con metas
- Unión de `df_casos_bd` con la pestaña **Meta** del Excel.
- Creación de `df_casos_union` con la siguiente estructura:
Red | Tipo | Fecha | Cant_Casos | Meta | % Cumplimiento

- Exportación a `df_casos_union.xlsx`.  
📂 Script: [`Ejercicio2.py`](Ejercicio2.py)

### 🔹 Ejercicio 3 – Consulta SQL
- Creación de una base SQLite en memoria.
- Inserción del DataFrame `df_casos_union`.
- Query para agrupar por Red, Tipo, Año y Mes, sumando casos:
```sql
SELECT
    Red,
    Tipo,
    strftime('%Y', Fecha) AS Año,
    strftime('%m', Fecha) AS Mes,
    SUM(Cant_Casos) AS Cant_Casos
FROM df_casos_union
GROUP BY Red, Tipo, strftime('%Y', Fecha), strftime('%m', Fecha);
```
Exportación del resultado a resultado_casos.xlsx.
📂 Script: Ejercicio3.py
📄 Consulta: consulta.txt

### 🔹 Ejercicio 4 – Control de versiones con Git
Creación de repositorio en GitHub.

Comandos utilizados: git init, git remote add origin, git add ., git commit -m, git push -u origin main.
📄 Explicación: Ejercicio 4.pdf

### 🔹 Ejercicio 5 – Dashboard en Power BI
Conexión directa a las pestañas Casos y Meta en Power BI (sin usar DataFrames).

Creación de un dashboard interactivo para responder preguntas como:

¿Cuál es el % de cumplimiento de casos?

¿Cómo ha sido el comportamiento de los casos por día?

¿Qué red y tipo concentran más casos?
📂 Archivo: PruebaBancolombia.pbix

🛠️ Tecnologías utilizadas
Python 3.9.12 (Pandas, XlsxWriter, SQLite3)
SQL (SQLite)
Power BI
Excel

📣 Autor
Miguel Gallego Álvarez
✉️ miguelgallego2020@gmail.com



