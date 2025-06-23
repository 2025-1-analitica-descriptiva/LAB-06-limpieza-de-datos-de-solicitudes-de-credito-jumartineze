"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


import pandas as pd

from ._internals.clean_data import clean_data
from ._internals.save_output import save_output


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"
    """
    data = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0).dropna()
    data = clean_data(data)
    save_output(data, "files/output", "solicitudes_de_credito.csv")