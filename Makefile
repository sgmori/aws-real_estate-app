install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C my-function/*.py
test:
	pytest test_hello.py
