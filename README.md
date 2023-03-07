# Open-Science-Practices
[![DOI](https://zenodo.org/badge/599046489.svg)](https://zenodo.org/badge/latestdoi/599046489)

Prácticas de la asignatura optativa Open Science de la UPM
Gonzalo Romeral Álvarez -- 2023


-Conectarse al host

-A través del cliente, sacar los xml de nuestros 10 papers

-Con la salida generar:
Dibuja una nube de palabras clave basada en la información del resumen.
Crea una visualización que muestre el número de figuras por artículo.
Crea una lista de los enlaces encontrados en cada documento.

#Instalación previa
- Python: https://www.python.org/downloads/
- Docker: https://www.docker.com/products/docker-desktop/
- Dependencias de python:
    -Grobid Client
    -Beautiful Soup
    -lxml
    -bs4
    -wordcloud  
    -matplotlib
    -Dependencias colaterales de las anteriores librerias
-Sistema operativo preferido: Windows 7+

#Ejecucion 
- Genera tu propio entorno a través de estos pasos
- Ejecutar las instrucciones del dockerfile, llamado docker_openScience.yml
- Para comprobar que hemos instalado todo en orden entramos http://localhost:8070/ y si todo va en orden debería estar funcionando nuestro cliente 
-Ejecutamos en nuestro entorno el script grobid_2.1.py a través de python, en nuestro entorno 
-Nos pedirá un directorio, debemos seleccionar aquel donde tengamos los pdfs, sino tiene pdfs el directorio saldrá error, y hay que ejecutar otra vez el script.
-En esta versión dejara los xml en el mismo directorio, para otra versión se podrá elegir el directorio de salida.
-Por último creará un documento, con los tres apartados de la nube de palabras, las figuras y los links.

Si surge algún problema, puedo solucionarlo si se me comenta con anterioridad
