import pandas as pd
import re

file_path = r"patient_data_GSE43488.xlsx" 
df = pd.read_excel(file_path)

df = df.map(lambda x: str(x).replace('gender: male', 'M').replace('gender: female', 'F') if isinstance(x, str) else x)

def convert_to_years(value):
    if isinstance(value, str):
        # Cerca i numeri all'interno della stringa
        match = re.search(r'age at sample \(months\): (\d+)', value)
        if match:
            months = int(match.group(1))
            years = months // 12  # Divisione intera per ottenere gli anni
            return years
    return value

df = df.map(convert_to_years)

def diagnosis_replacement(value):
    if isinstance(value, str):
        # Caso 1: Se la cella contiene "no T1D diagnosis"
        if "no T1D diagnosis" in value:
            return "Healthy"
        # Caso 2: Se la cella contiene "t1d diagnosis (months):" seguito da un numero
        match = re.search(r'(?:time from )?t1d diagnosis \(months\): -?\d+', value)
        if match:
            return "Type 1 Diabetes"
    return value

df = df.map(diagnosis_replacement)

df.to_excel(r"patient_data_GSE43488.xlsx", index=False)
