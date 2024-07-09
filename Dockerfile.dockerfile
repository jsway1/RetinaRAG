FROM python:3.10

WORKDIR /retinallmdocker

COPY . /retinallmdocker

RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5050 8080

# tried EXPOSE 5050 alone 

CMD [ "python", "./app.py" ]

# Docker run commands tried 

# docker build -t retinarag -f Dockerfile.dockerfile .

# docker run -p 5050:5050 -p 8080:8080 retinarag    

# docker run -p 5050:5050 -p 8080:8080 --add-host host.docker.internal:127.0.0.1 retinarag
