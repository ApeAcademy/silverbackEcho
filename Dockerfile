FROM apeworx/silverback:latest

WORKDIR /app
COPY ./bots/* ./bots/
COPY requirements.txt .
COPY ape-config.yaml .
RUN pip install --upgrade pip \
  && pip install -r requirements.txt
RUN ape plugins install .

CMD ["run", "bots.hollaback:app"]
