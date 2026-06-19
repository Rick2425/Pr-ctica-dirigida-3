# Parte 1: Programas en Red
# ==========================================
# LIBRERÍAS NECESARIAS
# ==========================================
from bs4 import BeautifulSoup
import pandas as pd
import re
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

# ==========================================
# PARTE II. RECUPERACIÓN DE DATOS
# ==========================================

# Página web asignada
url = "https://www.scrapethissite.com/pages/forms/"

# Encabezado para simular una petición desde navegador
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Obtener el contenido HTML de la página
response = requests.get(url, headers=headers)
response.raise_for_status()

# Analizar el HTML
soup = BeautifulSoup(response.text, "html.parser")

# Buscar las filas de la tabla
filas = soup.select("tr.team")

# Lista donde se guardarán los registros extraídos
registros = []

# Obtener al menos 15 registros
for fila in filas[:20]:

    # Texto completo de la fila
    texto_fila = fila.get_text(" ", strip=True)

    # Expresión regular para extraer un año de 4 dígitos
    patron_anio = re.search(r"\b(19|20)\d{2}\b", texto_fila)

    # Extraer atributos relevantes
    equipo = fila.select_one(".name").get_text(strip=True)
    anio = patron_anio.group() if patron_anio else None
    victorias = fila.select_one(".wins").get_text(strip=True)
    derrotas = fila.select_one(".losses").get_text(strip=True)
    porcentaje_victoria = fila.select_one(".pct").get_text(strip=True)

    # Guardar cada registro como diccionario
    registros.append({
        "equipo": equipo,
        "anio": anio,
        "victorias": victorias,
        "derrotas": derrotas,
        "porcentaje_victoria": porcentaje_victoria
    })

print("PARTE II - Registros recuperados:")
print(registros)
print("Cantidad de registros obtenidos:", len(registros))

