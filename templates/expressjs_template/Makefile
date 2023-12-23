update-version:
	bash bin/update_version_in_readme.sh

lint:
	npm run lint

format:
	npm run format

test:
	npm test

dev:
	npm run dev

start:
	npm start

run-scripts: update-version

# Docker specific targets
docker-script := ./bin/docker-script.sh

docker-build:
	$(docker-script) build

docker-run:
	$(docker-script) run

docker-stop:
	$(docker-script) stop

docker-clean:
	$(docker-script) clean

docker-test:
	$(docker-script) test


.PHONY: update-version format run-scripts
