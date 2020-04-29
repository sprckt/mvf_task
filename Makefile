SHELL:=/bin/bash
DOCKER_STACK_NAME:=mvf
GIT_USER:=

build:  ## build image for deployment
	docker build -t ${DOCKER_STACK_NAME} -f Dockerfile .

run: ## runs container, use like this make GIT_USER=xxxx run
	docker run -it --rm --name ${DOCKER_STACK_NAME}_run \
	--env-file .env \
	-t ${DOCKER_STACK_NAME}:latest \
	python github_poller.py -user ${GIT_USER}

test: # run pytest
	docker run -it --rm --name ${DOCKER_STACK_NAME}_test \
	--env-file .env \
	-t ${DOCKER_STACK_NAME}:latest \
	python -m pytest tests/ -s --verbose

help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'