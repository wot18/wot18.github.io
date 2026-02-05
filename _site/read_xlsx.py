import pandas as pd

filename = "各级研究生信息.xlsx"
try:
    df = pd.read_excel(filename, header=None) # Assume no header or we check first
    print(df.to_string())
except Exception as e:
    print(f"Error reading excel: {e}")
