from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.treinar_modelo import y_pred, y_test


print("Matriz de confusão:\n", confusion_matrix(y_test, y_pred))
print("\nRelatório de classificação:\n", classification_report(y_test, y_pred))
print("Acurácia:", accuracy_score(y_test, y_pred))