IMAGE_NAME=sihc/learning-jenkins
IMAGE_TAG?=latest
NEW_TAG?=latest
TARGET?=

run:
	PYTHONPATH=./src python src/app/__main__.py


clean:
	rm -rf $$(find . -type d -name __pycache__)
	rm -rf $$(find . -name *.pyc)


# Docker

docker-link-release:
	docker tag registry.gitlab.com/ap1n/${IMAGE_NAME}:${NEW_TAG} registry.gitlab.com/ap1n/${IMAGE_NAME}:latest

docker-remove-unsue-image:
	docker rmi $$(docker images --filter "dangling=true" -q --no-trunc) || TRUE


# Docker compose

dc-up:
	cd docker/jenkins && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose up ${TARGET}

dc-down:
	cd docker/jenkins && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose down ${TARGET}

dc-update:
	cd docker/jenkins && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose up --detach ${TARGET}

dc-build-update:
	cd docker/jenkins && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose up --detach --build ${TARGET}

dc-build:
	make clean
	cd docker/jenkins && \
		IMAGE_TAG=${NEW_TAG} docker-compose build ${TARGET}

dc-build-latest:
	make dc-build IMAGE_TAG=${NEW_TAG} TARGET=${TARGET}
	make docker-link-release NEW_TAG=${NEW_TAG}

dc-push:
	cd docker/jenkins && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose push ${TARGET}

dc-pull:
	cd docker/jenkins && \
		IMAGE_TAG=${IMAGE_TAG} docker-compose pull ${TARGET}

dc-reup:
	make dc-down dc-build dc-up NEW_TAGE=$(NEW_TAG) IMAGE_TAG=${NEW_TAG} TARGET=${TARGET}

dc-restart:
	make dc-pull dc-down dc-up IMAGE_TAG=${IMAGE_TAG} TARGET=${TARGET}
