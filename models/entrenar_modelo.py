import pickle
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Cargar dataset
digits = load_digits()
X, y = digits.data, digits.target

# Entrenar modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = SVC(gamma=0.001, random_state=42)
model.fit(X_train, y_train)

# Guardar modelo
model_filename = "./data/modelo_digits.pkl"
with open(model_filename, "wb") as file:
    pickle.dump(model, file)
