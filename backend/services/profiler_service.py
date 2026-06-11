import pandas as pd


def profile_dataset(df: pd.DataFrame):

    profile = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_profiles": []
    }

    for column in df.columns:

        col_data = {
            "name": column,
            "dtype": str(df[column].dtype)
        }

        if pd.api.types.is_numeric_dtype(df[column]):

            col_data["min"] = float(df[column].min())
            col_data["max"] = float(df[column].max())
            col_data["mean"] = float(df[column].mean())

        else:

            col_data["unique_values"] = int(
                df[column].nunique()
            )

        profile["column_profiles"].append(col_data)

    return profile