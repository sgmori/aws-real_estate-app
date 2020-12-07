install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C *.py
test:
	pytest tests/*.py

