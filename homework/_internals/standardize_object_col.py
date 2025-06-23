def standardize_object_col(df, column, strip=True):
    df = df.copy()

    series = df[column].str.lower().str.replace("_", " ", regex=False).str.replace("-", " ", regex=False)

    if strip:
        series = series.str.strip()

    df[column] = series
    return df