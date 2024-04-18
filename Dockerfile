FROM python:3.11-bookworm

WORKDIR /usr/src/schnitzel

COPY . .
RUN apt-get update && apt-get install ffmpeg -y && pip install -r requirements.txt

CMD ["python", "main.py"]