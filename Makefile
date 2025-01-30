# Makefile target args
args = $(filter-out $@,$(MAKECMDGOALS))

build: ;
	make down
	docker build -f Dockerfile --no-cache -t fastapi-di-backend .

up: ;
	docker-compose -f docker-compose.yml -p fastapi-di  up -d --build

down: ;
	docker-compose -f docker-compose.yml -p fastapi-di  down -t 0

restart: ;
	make down
	make up

enter: ;
	docker exec -it fastapi-di-backend bash
