import pandas as pd
import numpy as np

with open(r"txt\GSE9006-GPL97_series_matrix.txt", 'r') as file:
    lines = file.readlines()

geo_accession = []
metadata_list = []

current_metadata = []

for line in lines:
    if line.startswith('!Sample_geo_accession'):
        geo_accession = line.split('\t')[1:]  # Estrai gli ID pazienti, rimuovi descrizione iniziale
        geo_accession = [x.strip().replace('"', '') for x in geo_accession]  # Pulisci i doppi apici
    
    elif line.startswith('!Sample_source_name_ch1') or line.startswith('!Sample_characteristics_ch1'):
        current_metadata = line.split('\t')[1:]  # Estrai i dati dopo il tab
        current_metadata = [x.strip().replace('"', '') for x in current_metadata]  # Pulisci i dati
        metadata_list.append(current_metadata)  # Aggiungi i dati alla lista principale

print(metadata_list)
print(metadata_list[0])
print(metadata_list[1])

metadata_transposed = list(map(list, zip(*metadata_list)))  # Trasponi le liste

df = pd.DataFrame(columns=geo_accession)

for i, metadata in enumerate(metadata_list):
    for j, value in enumerate(metadata):
        df.loc[i, geo_accession[j]] = value

print(df.columns)

df.to_excel(r'HG-U133B_patients_data.xlsx', index=False)  # index=False per non salvare l'indice del DataFrame