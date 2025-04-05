import json
import joblib
import numpy as np
import pandas as pd
from azureml.core.model import Model

def init():
    global model, scaler, pca
    # Cargar el modelo entrenado desde el almacenamiento de Azure
    model_path = Model.get_model_path('model_act2')
    model = joblib.load(model_path)
    
    # Cargar el scaler y pca si están disponibles en el almacenamiento de Azure
    try:
        scaler_path = Model.get_model_path('scaler')
        pca_path = Model.get_model_path('pca')
        
        scaler = joblib.load(scaler_path) if scaler_path else None
        pca = joblib.load(pca_path) if pca_path else None
    except Exception as e:
        scaler = None
        pca = None
        print(f"Error loading scaler or pca: {e}")

def sigmoid(x):
    # Función sigmoide
    return [1 / (1 + np.exp(-y)) for y in x]

def run(raw_data):
    try:
        # Procesar los datos recibidos en el formato esperado
        data = json.loads(raw_data)['data'][0]
        data = pd.DataFrame(data)
        
        # Ajustar las columnas de entrada según las que el modelo espera
        expected_columns = ['ROA(C) before interest', 'ROA(A) before interest', 'Operating Gross Margin', 'Operating Profit Rate', 'Research and development expense rate', 'Cash Flow Rate', 'Interest-bearing debt interest rate', 'Tax rate (A)', 'Net Value Per Share (B)', 'Net Worth Turnover Rate (times)', 'Current Ratio', 'Working Capital/Equity', 'Cash Flow to Liability', 'Liability-Assets Flag']  # Asegúrate de ajustar esto con las columnas correctas
        data = data[expected_columns]
        
        # Aplicar las transformaciones necesarias si existen (Scaler y PCA)
        if scaler:
            data = scaler.transform(data)
        if pca:
            data = pca.transform(data)
        
        # Realizar la predicción con el modelo cargado
        result = model.predict(data).tolist()
        
        # Aplicar la función sigmoide y determinar el umbral
        result_sigmoid = sigmoid(result)
        umbral = 0.5
        result_final = [1 if x > umbral else 0 for x in result_sigmoid]
        
        return json.dumps(result_final)
    
    except Exception as e:
        # En caso de error, devolver el mensaje de error
        return json.dumps({"error": str(e)})

