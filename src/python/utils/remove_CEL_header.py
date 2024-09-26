import pandas as pd

file_path = r"HG-U133A_collapsed_data.xlsx"
df = pd.read_excel(file_path)

df.columns = [col.replace('.CEL', '') for col in df.columns]

output_file_path = r"HG-U133A_collapsed_data_noCEL.xlsx"
df.to_excel(output_file_path, index=False)

print("Nomi delle colonne modificati e file salvato.")
