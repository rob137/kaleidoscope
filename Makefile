install:
	pip install -r requirements.txt

run:
	python main.py images/test.png 3

lint:
	ruff check .

format:
	ruff format .