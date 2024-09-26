import pandas as pd

df = pd.read_excel(r'..\..\xlsx\xlsx_GSE43488\GSE43488_mapped.xlsx')

df = df.assign(SYMBOL=df['SYMBOL'].fillna('NA'))

df_cleaned = df[df['SYMBOL'] != 'NA']

df_cleaned.to_excel(r'..\..\xlsx\xlsx_GSE43488\GSE43488_mapped_ciao.xlsx', index=False)
