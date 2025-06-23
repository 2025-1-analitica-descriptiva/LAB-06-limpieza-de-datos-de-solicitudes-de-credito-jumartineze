import pandas as pd


def standardize_dates(df, column):
    df = df.copy()

    # Convierte todo a string para evitar errores
    series = df[column].astype(str)

    # Detecta si la fecha empieza por 4 dígitos (año al principio)
    mask_year_first = series.str.match(r"^\d{4}/\d{1,2}/\d{1,2}$")

    # Procesa año al principio
    df.loc[mask_year_first, column] = pd.to_datetime(
        series[mask_year_first], format="%Y/%m/%d", errors="coerce"
    ).dt.strftime("%d/%m/%Y")

    # Procesa fechas con día/mes al principio
    df.loc[~mask_year_first, column] = pd.to_datetime(
        series[~mask_year_first], dayfirst=True, errors="coerce"
    ).dt.strftime("%d/%m/%Y")

    # Reemplaza valores no convertidos (NaT) por NA
    df[column] = df[column].where(df[column].notna(), pd.NA)

    return df