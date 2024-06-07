FROM python:3.11-bookworm

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "silverback", "run", "bots.hollaback:app"]

#docker run -e ETHERSCAN_API_KEY=$ETHERSCAN_API_KEY 
#-it testing:latest --network :sepolia:node