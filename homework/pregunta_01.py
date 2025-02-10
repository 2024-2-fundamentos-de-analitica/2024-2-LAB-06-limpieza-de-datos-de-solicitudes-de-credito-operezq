"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    

    df["sexo"] = df["sexo"].str.strip().str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower().str.strip()
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("_"," ").str.replace("-"," ").str.strip()
    df["barrio"] = df["barrio"].str.lower().str.replace("_"," ").str.replace("-"," ")
    df["estrato"] = df["estrato"].astype(int)
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format="mixed")
    df["monto_del_credito"] = df["monto_del_credito"].str.strip().str.replace("$","").str.replace(",","").str.replace(".00","").astype(float)
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip("_").str.strip("-").str.strip().str.replace("_"," ").str.replace("-"," ") 
    

    df = df.dropna()
    df = df.drop_duplicates()

    df.to_csv("files/output/solicitudes_de_credito.csv", sep=';', index=False)

    return df


print(pregunta_01())