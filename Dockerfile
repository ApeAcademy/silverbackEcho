FROM apeworx/silverback:latest

USER harambe
RUN mkdir ~/.aws

WORKDIR /app
COPY ./bots/* ./bots/
COPY requirements.txt .
COPY ape-config.yaml .

RUN pip install --upgrade pip \
  && pip install -r requirements.txt

RUN ape plugins install .
