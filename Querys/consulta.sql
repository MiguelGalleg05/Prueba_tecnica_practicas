 
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
