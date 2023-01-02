FROM pypy:latest

WORKDIR /app
COPY . /app
CMD /watch_next.py

RUN pip install -r requirements.txt