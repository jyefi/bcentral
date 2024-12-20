import os
import requests
import json
import time
import pandas as pd

time_start=time.time()

user=os.environ.get('BANCO_CENTRAL_USER')
passwd=os.environ.get('BANCO_CENTRAL_PASSWORD')

firstdate="2024-12-01"
lastdate="2024-12-20"

#código de serie (EUR)
serie="F072.CLP.EUR.N.O.D"

URL = f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user={user}&pass={passwd}&firstdate={firstdate}&lastdate={lastdate}&timeseries={serie}&function=GetSeries"

response = requests.get(URL)
print(f"Código de respuesta http: {response.status_code}")
respuesta = response.json()
time_end=time.time()
print(f"Tiempo de ejecución: {time_end - time_start:.2f} segundos")

print("Respuesta (original) formateada:")
print(json.dumps(respuesta, indent=4))

#Se convierte la respuesta en un diccionario
data = {
    obs["indexDateString"]: obs["value"]
    for obs in respuesta["Series"]["Obs"]
    if obs["statusCode"] == "OK"
}

print("Datos extraídos (diccionario):")
print(data)

# Convert the dictionary to a DataFrame
df = pd.DataFrame(list(data.items()), columns=['Fecha', 'Valor'])
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d-%m-%Y')
df['Valor'] = df['Valor'].astype(float).round(2)

# Save the DataFrame to an Excel file
output_file = "bcentral_data.xlsx"
df.to_excel(output_file, index=False)

print(f"Datos guardados en el archivo: {output_file}")