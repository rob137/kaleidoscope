# Kaleidoscope

This project uses Google's Gemini 2.0 Flash Preview Image Generation model to generate image variations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/kaleidoscope.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables by creating a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

Note: You can obtain a Google API key from the [Google AI Studio](https://aistudio.google.com/) console.

## Usage

Run the `main.py` script with the path to the initial image and the number of variations to generate.

```bash
python main.py <image_path> <count>
```

### Examples

```bash
# Generate 5 variations of a local image
python main.py outputs/test.png 5

# Generate 3 variations of any image file
python main.py /path/to/your/photo.jpg 3

# Quick test run (uses predefined example)
make run
```

### Available Make Commands

```bash
make help     # Show all available commands
make install  # Install dependencies
make run      # Run example with outputs/test.png and 3 variations
make lint     # Run code linting
make format   # Format code
```

Generated variations will be saved in the `outputs` directory with timestamps.
