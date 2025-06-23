def remove_duplicates(df):
    df = df.copy()
    df = df.drop_duplicates().reset_index(drop=True)
    return df