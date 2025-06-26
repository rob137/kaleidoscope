help:
	@echo "Available commands:"
	@echo "  install  - Install dependencies from requirements.txt"
	@echo "  run      - Generate 3 variations of outputs/test.png using OpenAI"
	@echo "  lint     - Run ruff linting"
	@echo "  format   - Run ruff formatting"
	@echo ""
	@echo "Usage: python main.py <image_path> <count>"
	@echo "       Creates <count> AI-generated variations of input image"
	@echo "Example: python main.py path/to/image.jpg 5"
	@echo "         Generates 5 variations and saves to outputs/ directory"

install:
	pip install -r requirements.txt

run:
	@echo "Running example with outputs/test.png and 3 variations..."
	python main.py outputs/test.png 3

lint:
	ruff check .

format:
	ruff format .