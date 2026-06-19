# Parte 1: Programas en Red

import requests

# 1. Definir la URL objetivo
url = "https://www.scrapethissite.com/pages/forms/"

try:
    # 2. Realizar la petición HTTP GET
    response = requests.get(url)
    
    # Levantar una excepción si hubo un error en la petición HTTP (códigos 4xx o 5xx)
    response.raise_for_status()
    
    print("--- Resultados de la Conexión ---")
    
    # 3. Mostrar el status_code
    print(f"Status Code: {response.status_code}")
    
    # 4. Mostrar la URL consultada
    print(f"URL Consultada: {response.url}")
    
    # 5. Mostrar el Content-Type
    print(f"Content-Type: {response.headers.get('Content-Type')}")

except requests.exceptions.RequestException as e:
    print(f"Error al intentar conectar con la página: {e}")
