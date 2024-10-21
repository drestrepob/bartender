include .env

# Alias
awslocal=aws --endpoint-url http://localhost:4566
clean-flags=--volumes --rmi all --remove-orphans
dc=docker compose


build:
	$(dc) up --build

start:
	$(dc) up

bash:
	$(dc) exec -it backend bash

clean:
	$(dc) down $(clean-flags)
