import pandas as pd

expression_data = pd.read_excel(r"dataset_without_patient_data.xlsx")

metadata = pd.read_excel(r"HG-U133A_patients_data")

print(metadata.columns)
print(expression_data.columns)

expression_data_t = expression_data.T
metadata_t = metadata.T

print(expression_data_t.head())
print(metadata_t.head())

# Left join
merged_data = pd.merge(expression_data_t, metadata_t, left_index=True, right_index=True, how='left')

print("Dataset unito:")
print(merged_data.head())

merged_data_t = merged_data.T
print(merged_data_t)

merged_data_t.to_excel(r"dataset1_with_T2D", index=False)