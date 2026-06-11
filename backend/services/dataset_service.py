import pandas as pd


def load_dataset(file_path: str):
    df = pd.read_csv(file_path)

    print("\nDataset Loaded Successfully\n")

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nPreview:")
    print(df.head())

    return df