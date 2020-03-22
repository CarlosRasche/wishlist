format:
	isort --recursive .
	black .

freeze:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --no-index --output-file requirements.txt setup.py

freeze-upgrade:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --no-index --upgrade --output-file requirements.txt setup.py

run:
	python server.py