setup:
	python3 -m venv ~/.aws-real_estate-app

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest tests/*.py

lint:
	pylint --disable=R,C flaskdynamodb dynamo-batch-writer

all: install lint test


