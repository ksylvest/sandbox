FROM python:3.13.1-slim

WORKDIR /project

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD [ "fastapi", "run", "--host", "0.0.0.0", "--port", "8000", "main.py" ]
