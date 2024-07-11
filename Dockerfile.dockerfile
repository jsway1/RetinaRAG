FROM python:3.10

WORKDIR /retinallmdocker

COPY . /retinallmdocker

RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5050 

CMD [ "python", "./app.py" ]
