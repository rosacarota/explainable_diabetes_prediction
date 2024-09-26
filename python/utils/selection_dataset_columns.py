import pandas as pd
import numpy as np

dataset = pd.read_excel(r'Operazioni\t-test.xlsx')
columns_list = open(r'txt\geni.txt', 'r').readlines()
print(columns_list)

for i in range(len(columns_list)):
    columns_list[i] = columns_list[i].replace('\n', '')

print(columns_list)
for column in dataset.columns:
    if column not in columns_list:
        dataset = dataset.drop(column, axis=1)

dataset.to_excel(r'Operazioni\dataset.xlsx', index=False)