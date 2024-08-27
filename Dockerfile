FROM python:3.11 AS base

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /build

# Create virtualenv using poetry lockfile
FROM base AS builder

FROM apeworx/silverback:latest

USER root
RUN apt-get -y update && apt-get -y install git

# Is this necessary after a real tagged release?
ENV SETUPTOOLS_SCM_PRETEND_VERSION="6.6.6"

ENV PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.6.1

WORKDIR /app
RUN mkdir -p .build && chown harambe:harambe .build

USER harambe
RUN mkdir ~/.aws

COPY --chown=harambe:harambe ./bots/* ./bots/
COPY --chown=harambe:harambe ./contracts/* ./contracts/

COPY ape-config.yaml ape-config.yaml
COPY requirements.txt .
RUN pip install --upgrade pip \
  && pip install -r requirements.txt

RUN ape plugins install .

RUN ape tokens install https://tokens.coingecko.com/uniswap/all.json
RUN ape compile

ENV WORKERS=1
ENV MAX_EXCEPTIONS=3
ENV SILVERBACK_NETWROK_CHOICE=ethereum:sepolia:alchemy

ENV STABILITY_KEY=
ENV PINATA_API_KEY=
ENV PINATA_SECRET_API_KEY=
ENV ECHO_CONTRACT=
ENV APE_ACCOUNT_ALIAS=

ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=
ENV AWS_DEFAULT_REGION=

ENTRYPOINT silverback worker -v DEBUG -w $WORKERS \
  -x $MAX_EXCEPTIONS --account bot "bots.hollaback:app"
