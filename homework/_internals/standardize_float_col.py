def standardize_float_col(df, column):
    df = df.copy()
    df[column] = (
        df[column]
        .str.replace(" ", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )
    return df