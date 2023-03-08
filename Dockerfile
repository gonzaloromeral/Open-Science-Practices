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

# To build the image, we use the following command (replace "myimage" with the name you want to give it): docker build -t myimage .
# To run the script, we use: docker run --rm -it -v /local_directory:/app myimage
# We need to replace the local directory with the directory where the Python script is located.
