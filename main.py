import argparse
import base64
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def generate_image_variation(image_path, iteration):
    """
    Generates an image variation using the OpenAI gpt-4.1 model.
    """
    print(f"Generating variation {iteration} from {image_path}...")
    base64_image = encode_image(image_path)
    prompt = "Recreate this image"

    try:
        response = client.responses.create(
            model="gpt-4o",
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": prompt},
                        {
                            "type": "input_image",
                            "image_url": f"data:image/png;base64,{base64_image}",
                        },
                    ],
                }
            ],
            tools=[{"type": "image_generation"}],
        )

        image_generation_calls = [
            output
            for output in response.output
            if output.type == "image_generation_call"
        ]

        if image_generation_calls:
            image_base64 = image_generation_calls[0].result
            new_image_path = f"images/variation_{iteration}.png"
            with open(new_image_path, "wb") as f:
                f.write(base64.b64decode(image_base64))
            return new_image_path
        else:
            # Look for text content if image generation failed
            text_content = [
                output.text
                for output in response.output
                if output.type == "text"
            ]
            if text_content:
                raise Exception(f"Image generation failed: {text_content[0]}")
            else:
                raise Exception("Image generation failed. No image data in response.")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Generate image variations using OpenAI's gpt-4.1 model."
    )
    parser.add_argument("image_path", type=str, help="The path to the initial image.")
    parser.add_argument(
        "count", type=int, help="The number of variations to generate."
    )
    args = parser.parse_args()

    if not os.path.exists("images"):
        os.makedirs("images")

    current_image_path = args.image_path
    for i in range(args.count):
        current_image_path = generate_image_variation(current_image_path, i + 1)
        print(f"Saved new image to {current_image_path}")


if __name__ == "__main__":
    main()
