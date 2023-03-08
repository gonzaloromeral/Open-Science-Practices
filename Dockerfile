#Not tested yet
FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libxml2-dev \
        libxslt-dev \
        zlib1g-dev \
        libffi-dev \
        libssl-dev \
        && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
        grobid-client \
        beautifulsoup4 \
        matplotlib \
        wordcloud

WORKDIR /app

COPY grobid_2.1.py .

ENTRYPOINT ["python", "grobid_2.1.py"]

# Para buildear la imagen usamos el siguiente comando(miimagen es el nombre que le quieras poner): docker build -t miimagen .
# Para correr el script hacemos: docker run --rm -it -v /directorio_local:/app miimagen
# Tenemos que sustituir el directorio local por donde el script de python
