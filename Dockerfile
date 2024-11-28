FROM python:3.13.0-slim

WORKDIR /project

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app

ARG PORT = 8000
ENV PORT $PORT
EXPOSE $PORT

CMD [ "fastapi", "run", "--host", "0.0.0.0", "--port", $PORT, "app/main.py" ]
