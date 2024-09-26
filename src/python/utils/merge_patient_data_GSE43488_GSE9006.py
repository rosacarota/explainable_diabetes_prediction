import pandas as pd

metadata_gse9006 = pd.read_excel(r"HG-U133A_patients_data")

metadata_gse43488 = pd.read_excel(r"patient_data_GSE43488.xlsx")

print(metadata_gse9006.columns)
print(metadata_gse43488.columns)

merged_data = pd.concat([metadata_gse9006, metadata_gse43488], axis=1)

print("Dataset unito:")
print(merged_data.head())

merged_data.to_excel(r"dataset1_patient_data.xlsx", index=False)
