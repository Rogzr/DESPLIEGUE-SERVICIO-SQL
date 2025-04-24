import json
import joblib
import numpy as np
import pandas as pd
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('modifiedate_model')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data'][0]
        data = pd.DataFrame(data)

        # Seleccionar columnas relevantes
        data = data[['CompanyName', 'SalesPerson', 'ModifiedDate']]

        # Convertir ModifiedDate a datetime y luego a rango de días
        data['ModifiedDate'] = pd.to_datetime(data['ModifiedDate'])
        data['Fecha'] = (data['ModifiedDate'] - data['ModifiedDate'].min()).dt.days

        # Eliminar columna original
        data.drop(columns=['ModifiedDate'], inplace=True)

        # Realizar predicción usando solo la columna transformada
        result = model.predict(data[['Fecha']])

        return json.dumps({"result": result.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})

