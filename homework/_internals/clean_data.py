from .remove_duplicates import remove_duplicates
from .standardize_dates import standardize_dates
from .standardize_float_col import standardize_float_col
from .standardize_object_col import standardize_object_col


def clean_data(df):
    df = standardize_object_col(df, "sexo")
    df = standardize_object_col(df, "tipo_de_emprendimiento")
    df = standardize_object_col(df, "idea_negocio")
    df = standardize_object_col(df, "barrio", strip=False)
    df = standardize_object_col(df, "línea_credito")
    df = standardize_dates(df, "fecha_de_beneficio")
    df = standardize_float_col(df, "monto_del_credito")
    df = remove_duplicates(df)
    return df