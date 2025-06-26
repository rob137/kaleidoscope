# Kaleidoscope

This project uses OpenAI's gpt-4o model to generate image variations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/kaleidoscope.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables by creating a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key
   ```

## Usage

Run the `main.py` script with the path to the initial image and the number of variations to generate.

```bash
python main.py <image_path> <count>
```

For example:

```bash
python main.py images/test.png 5
```

This will generate 5 variations of the `test.png` image and save them in the `images` directory.
