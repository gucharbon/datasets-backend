.SHELL := /usr/bin/env bash

dev-services:
	docker stack deploy -c compose/docker-compose.yml -c compose/dev.yml backend-dev

dev:
	datasets dev
