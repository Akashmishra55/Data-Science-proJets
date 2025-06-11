import pandas as pd
import os

# Set the path to your Excel file
EXCEL_FILE_PATH = os.path.join(os.path.dirname(__file__), "capbudg.xls")

def list_tables():
    try:
        excel_file = pd.ExcelFile(EXCEL_FILE_PATH)
        return {"tables": excel_file.sheet_names}
    except Exception as e:
        raise RuntimeError(f"Error reading Excel file: {e}")

def get_table_details(sheet_name: str):
    try:
        df = pd.read_excel(EXCEL_FILE_PATH, sheet_name=sheet_name)
        return df.to_dict(orient="records")
    except Exception as e:
        raise RuntimeError(f"Error reading sheet '{sheet_name}': {e}")

def row_sum(sheet_name: str, row_index: int):
    try:
        df = pd.read_excel(EXCEL_FILE_PATH, sheet_name=sheet_name)
        numeric_values = df.iloc[row_index].select_dtypes(include='number')
        if numeric_values.empty:
            return {"sum": 0}
        return {"sum": numeric_values.sum()}
    except Exception as e:
        raise RuntimeError(f"Error calculating row sum: {e}")
