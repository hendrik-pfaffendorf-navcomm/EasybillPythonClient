SPEC_URL = https://api.easybill.de/rest/v1/swagger.json
CONVERT_URL = https://converter.swagger.io/api/convert

all:
	setup-env
	refresh

setup-env:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

refresh:
	curl -X 'GET' '$(SPEC_URL)' | \
		curl -X 'POST' '$(CONVERT_URL)' \
		-H 'accept: application/yaml' \
		-H 'Content-Type: application/json' \
		-d @- | \
		sed '/^"null"/!s/"null"/null/g' | \
		openapi-python-client generate \
			--config openapi-python-client-config.yaml \
			--path /dev/stdin \
			--output-path easybill_client_package \
			--overwrite