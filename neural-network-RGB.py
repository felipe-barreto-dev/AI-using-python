# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle

# Definindo cores e seus respectivos espectros
cores = {
    'Vermelho': [(255, 0, 0), (200, 0, 0), (150, 0, 0)],
    'Verde': [(0, 255, 0), (0, 200, 0), (0, 150, 0)],
    'Azul': [(0, 0, 255), (0, 0, 200), (0, 0, 150)],
    'Amarelo': [(255, 255, 0), (200, 200, 0), (150, 150, 0)],
    'Ciano': [(0, 255, 255), (0, 200, 200), (0, 150, 150)],
    'Magenta': [(255, 0, 255), (200, 0, 200), (150, 0, 150)],
    'Laranja': [(255, 165, 0), (200, 130, 0), (150, 100, 0)],
    'Roxo': [(128, 0, 128), (100, 0, 100), (75, 0, 75)]
}

# Criando listas para armazenar os dados
X = []
y = []

# Preenchendo as listas com os dados
for espectro, valores_rgb in cores.items():
    for rgb in valores_rgb:
        X.append(rgb)
        y.append(espectro)

# Convertendo para arrays numpy
X = np.array(X)
y = np.array(y)

# Embaralhando os dados
X, y = shuffle(X, y, random_state=42)

# Codificando as labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Dividindo em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Normalizando os dados (valores RGB variam de 0 a 255)
X_train = X_train / 255.0
X_test = X_test / 255.0

# Definindo o modelo
model = Sequential()
model.add(Dense(64, input_dim=3, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(len(le.classes_), activation='softmax'))

# Compilando o modelo
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinando o modelo
history = model.fit(X_train, y_train, epochs=50, batch_size=5, validation_data=(X_test, y_test))

# Avaliando o desempenho no conjunto de teste
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Acurácia no conjunto de teste: {accuracy * 100:.2f}%')

# Função para prever o espectro de uma nova cor
def prever_espectro(r, g, b):
    rgb_norm = np.array([[r, g, b]]) / 255.0
    prediction = model.predict(rgb_norm)
    index = np.argmax(prediction)
    espectro = le.inverse_transform([index])
    return espectro[0]

# Exemplo de uso
nova_cor = (11, 141, 255)
espectro_previsto = prever_espectro(*nova_cor)
print(f'O espectro previsto para a cor {nova_cor} é: {espectro_previsto}')
