FROM python:2.7

COPY . /code
WORKDIR /code
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "runserver.py"]
