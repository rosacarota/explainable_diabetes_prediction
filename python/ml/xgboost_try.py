import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

file_path = r'D:\Uni\Tesi\Dataset\xlsx\Dataset_1\Operazioni\lasso.xlsx'
dataset = pd.read_excel(file_path)

X = dataset.drop(columns=['Illness', 'Age', 'Gender', 'ID_REF']) 
y = dataset['Illness']

# Trasforma Healthy in 0 e Type 1 Diabetes in 1
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Metriche
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1-Score: {f1}')
print(f'Confusion Matrix:\n{conf_matrix}')

# Visualizza il report completo di classificazione
classification_rep = classification_report(y_test, y_pred, target_names=['Healthy', 'Type 1 Diabetes'])
print(f'\nClassification Report:\n{classification_rep}')