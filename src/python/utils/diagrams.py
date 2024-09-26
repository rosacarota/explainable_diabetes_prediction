import pandas as pd
import matplotlib.pyplot as plt

file_path = r'dataset.xlsx'  # Percorso del file Excel
data = pd.read_excel(file_path)

gene_expression_data = data.drop(columns=['ID_REF', 'Illness', 'Age', 'Gender'])

# Istogramma
plt.figure(figsize=(10, 6))
gene_expression_data.stack().hist(bins=50)
plt.title('Distribuzione dei livelli di espressione')
plt.xlabel('Livello di espressione')
plt.ylabel('Frequenza')
plt.tight_layout()


plt.savefig(r'istogramma.png', format='png')

plt.show()

for threshold in [2, 5, 10]:  # Prova diverse soglie
    expressed_genes = gene_expression_data.apply(lambda row: row[row > threshold].count() > (len(row) / 2), axis=1)
    filtered_data = gene_expression_data[expressed_genes]
    print(f"Con soglia {threshold}, rimangono {filtered_data.shape[0]} geni.")

plt.figure(figsize=(40, 30))  # Imposta una dimensione maggiore per il grafico

gene_expression_data.boxplot()
plt.title('Distribuzione delle espressioni geniche per campione', fontsize=16)
plt.xlabel('Campioni', fontsize=14)
plt.ylabel('Espressione genica', fontsize=14)

plt.xticks(rotation=90, fontsize=6)
plt.tight_layout()

plt.savefig(r'boxplot.png', format='png')  # Salva come file PNG
