import pandas as pd

# Carica i due file Excel
file1 = r'dataset1.xlsx'
file2 = r'collapsed_data_GSE43488.xlsx'

# Leggi i file Excel nelle DataFrame, assicurandoti che l'ID_REF sia la chiave primaria
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Effettua un join sulle colonne ID_REF mantenendo solo le righe comuni (inner join)
merged_df = pd.merge(df1, df2, on='ID_REF', how='inner')
# Salva il risultato in un nuovo file Excel
merged_df.to_excel(r'dataset1_without_metadata.xlsx', index=False)

print("Join completato. I dati comuni sono stati salvati in 'merged_output.xlsx'.")
