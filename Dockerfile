FROM apeworx/silverback:latest

WORKDIR /app
COPY ./bots/* ./bots
COPY requirements.txt .
RUN pip install --upgrade pip \
  && pip install -r requirements.txt

