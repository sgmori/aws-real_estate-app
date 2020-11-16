install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C
test:
	pytest test_hello.py
