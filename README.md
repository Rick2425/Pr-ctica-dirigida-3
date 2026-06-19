<h1 align="center"> <b>UNIVERSIDAD NACIONAL AGRARIA LA MOLINA</b> </h3>
<h2 align="center"> <b>DEPARTAMENTO ACADÉMICO DE ESTADÍSTICA E INFORMÁTICA</b> </h2>
<p align="center">
  <img src="https://seeklogo.com/images/U/universidad-nacional-agraria-la-molina-logo-5BF0B8D973-seeklogo.com.png" 
       alt="La Molina Perú" 
       width="170" 
       height="170">
</p>
<h3 align="center">
<h3 align="center"> Práctica dirigida 3:  Análisis de la editorial 'BookAnalytics' para identificar oportunidades comerciales </h3> 
<h3> <b>Integrantes del equipo:</b> </h3>
<ul>
  <li>Cardenas Panduro, Ricardo Gabriel (Rick2425) (20241376) </li>
  <li>Tuppia Paitan, Joaquin Francisco (JTPXD) (20241405) </li>
  <li>Almonacid Quispe, Jimmy Salomón (patatita1theoriginal) (20241374) </li>
  <li>Ortiz Huamani, Ricardo Fidel (ricardofortizh) (20240724) </li>
  <il>Prompt de Joaquin( parte 2): 

"Actúa como un experto en web scraping con Python. Necesito extraer los datos de la página https://www.scrapethissite.com/pages/forms/ usando requests y BeautifulSoup. Por favor, incluye un User-Agent en los headers para simular un navegador. Usa selectores CSS (soup.select) para encontrar las filas con la clase 'team'. Extrae los primeros 20 registros y obtén: nombre del equipo, victorias, derrotas y porcentaje de victorias usando sus respectivas clases CSS (.name, .wins, .losses, .pct). Además, para practicar Regex, une todo el texto de la fila y usa la librería re para extraer el año buscando un patrón de 4 dígitos que empiece estrictamente con 19 o 20. Guarda todo en una lista de diccionarios." 
Prompt de  Ricardo (parte 3): 

Parte II. Recuperación de Datos (6 puntos) • Obtenga al menos 15 registros desde la página web o API. (2 ptos) • Extraiga tres atributos relevantes para el análisis. (2 ptos) • Utilice al menos una expresión regular para limpiar o extraer un patrón (precio, fecha, código, correo, etc.). (2 ptos) D. IMDB Top Movies (https://www.scrapethissite.com/pages/forms/) Ayudame a hacer esta parte del trabajo, añade las librerias para cumplir con los requisitos requeridos </il>

  ![Gráfico de resultados](imagen.jpeg)
  <li>Tengo un archivo llamado registros_hockey_scrapethissite.csv, generado a partir de datos extraídos de la página Scrape This Site sobre equipos de hockey.

Necesito desarrollar la *Parte IV. Visualización (2 puntos)* de mi trabajo, cumpliendo con el siguiente requisito:

* Generar un gráfico adecuado, puede ser de barras, líneas o pastel.
* Interpretar brevemente el resultado.

Quiero que el código esté hecho en *R con ggplot2* y que use una estética similar a este estilo:

* Gráfico de barras horizontal usando geom_col().
* Ordenar las categorías con reorder().
* Usar coord_flip().
* Añadir etiquetas con geom_text().
* Usar theme_bw().
* Quitar la leyenda.
* Título centrado, en negrita.
* Subtítulo centrado.
* Fondo del panel color khaki1.
* Texto del eje Y en color blue4, tamaño 9 y negrita.
* Ticks en color lightblue.
* Quitar líneas menores y líneas principales del eje Y.
* Guardar el gráfico con ggsave() en formato PNG, con ancho 9, alto 5 y resolución 300 dpi.

El gráfico debe usar el archivo registros_hockey_scrapethissite.csv.
La variable principal recomendada es porcentaje_victoria, para mostrar el *Top 10 equipos con mayor porcentaje de victoria*.
También debe crear una columna combinada llamada equipo_anio, uniendo el nombre del equipo y el año.

El código debe incluir:

1. Carga de librerías.
2. Lectura del CSV.
3. Transformación de variables numéricas.
4. Creación del Top 10.
5. Gráfico con estética personalizada.
6. Guardado del gráfico.
7. Interpretación breve del resultado con cat().

Dame solo el código completo en R, bien comentado y separado por secciones</li>


</ul>
