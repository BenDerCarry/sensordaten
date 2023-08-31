import pandas as pd
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

df = pd.read_csv('aggData.csv')
# df = pd.read_csv('small_aggData.csv')

X = df[['accX', 'accY', 'accZ', 'Vorheriges_Label']]
y = df[['label']]
X_encoded = pd.get_dummies(X)

# zufälliger Test/Train Split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3)

# SVM-Modell erstellen
model = svm.SVC(kernel='linear')

# Modell auf Trainingsdaten trainieren
model.fit(X_train, y_train)

# Vorhersagen für Testdaten machen
y_pred = model.predict(X_test)

# Vorhersage für Trainingsdaten als Vergleich
y_pred_train = model.predict(X_train)

# Genauigkeit der Vorhersagen berechnen
accuracy = accuracy_score(y_test, y_pred)
print("Genauigkeit:", accuracy)

accuracy_train = accuracy_score(y_train, y_pred_train)
print("Genauigkeit des Trainingssets:", accuracy_train)

# Confusion Matrix berechnen
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

classes = y_test['label'].unique()

# Confusion Matrix als Heatmap darstellen
sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=classes, yticklabels=classes)
plt.xlabel('Vorhergesagte Werte')
plt.ylabel('Echte Werte')
plt.title('Confusion Matrix')
plt.show()
