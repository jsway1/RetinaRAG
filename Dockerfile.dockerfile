FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5050

CMD [ "python", "./app.py" ]
