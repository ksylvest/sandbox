FROM python:3.13.0-slim

WORKDIR /project

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app

ENV PORT 8000
EXPOSE $PORT
CMD [ "fastapi", "run", "--host", "0.0.0.0", "--port", $PORT, "app/main.py" ]
