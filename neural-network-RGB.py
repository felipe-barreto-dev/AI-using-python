# Importando as bibliotecas necessárias
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Função para categorizar a cor com base no valor RGB
def categorize_color(rgb):
    r, g, b = rgb
    if r < 30 and g < 30 and b < 30:
        return 'preto'
    elif r > 225 and g > 225 and b > 225:
        return 'branco'
    elif r > 200 and g < 50 and b < 50:
        return 'vermelho'
    elif r < 50 and g > 200 and b < 50:
        return 'verde'
    elif r < 50 and g < 50 and b > 200:
        return 'azul'
    elif r > 200 and g > 200 and b < 50:
        return 'amarelo'
    elif r < 50 and g > 200 and b > 200:
        return 'ciano'
    elif r > 200 and g < 50 and b > 200:
        return 'magenta'
    elif r > 150 and g > 150 and b > 150:
        return 'cinza claro'
    elif r < 150 and g < 150 and b < 150:
        return 'cinza'
    elif r > 100 and g < 100 and b < 100:
        return 'marrom'
    elif r < 100 and g > 100 and b < 100:
        return 'verde escuro'
    elif r < 100 and g < 100 and b > 100:
        return 'azul escuro'
    else:
        return 'desconhecido'

# Gerar dataset de cores aleatórias e suas respectivas classificações
def generate_color_data(num_samples=1000):
    data = []
    labels = []
    for _ in range(num_samples):
        # Gerar cores RGB aleatórias
        rgb = np.random.randint(0, 256, 3)
        color = categorize_color(rgb)
        if color != 'desconhecido':  # Ignorar rótulos desconhecidos
            data.append(rgb)
            labels.append(color)
    
    # Converter para arrays numpy
    data = np.array(data, dtype=np.float32)
    labels = np.array(labels)
    
    # Normalizar valores RGB (de 0-255 para 0-1)
    data /= 255.0
    
    return data, labels

# Gerar os dados RGB e seus rótulos
X, y = generate_color_data(5000)  # Vamos gerar 5000 amostras aleatórias

# Codificar os rótulos para valores numéricos
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Converter rótulos para a forma categórica (one-hot encoding)
y_categorical = to_categorical(y_encoded)

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.2, random_state=42)

# Criar a rede neural
model = Sequential()

# Camada de entrada (3 neurônios para RGB), camada oculta com 64 neurônios, função de ativação ReLU
model.add(Dense(64, input_shape=(3,), activation='relu'))

# Outra camada oculta com 64 neurônios, função de ativação ReLU
model.add(Dense(64, activation='relu'))

# Camada de saída com o número de neurônios igual ao número de classes (cores) e função softmax
model.add(Dense(y_categorical.shape[1], activation='softmax'))

# Compilar o modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Avaliar o modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Acurácia no conjunto de teste: {accuracy * 100:.2f}%')

# Função para prever a cor com base no valor RGB
def predict_color(rgb):
    # Normalizar o valor RGB (de 0-255 para 0-1)
    rgb_normalized = np.array(rgb).reshape(1, -1) / 255.0
    # Prever a classe
    prediction = model.predict(rgb_normalized)
    # Obter a cor prevista (índice da classe com maior probabilidade)
    color_index = np.argmax(prediction)
    # Converter o índice de volta para o nome da cor
    return encoder.inverse_transform([color_index])[0]

# Testar a função com alguns exemplos
test_rgb = [0, 0, 0]  # Exemplo de valor RGB para teste
predicted_color = predict_color(test_rgb)
print(f'A cor prevista para RGB {test_rgb} é {predicted_color}')
