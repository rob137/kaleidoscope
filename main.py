import argparse
import os
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_image_variation(image_path, iteration):
    """
    Generates an image variation using the Google Gemini 2.0 Flash Preview Image Generation model.
    """
    print(f"Generating variation {iteration} from {image_path}...")
    
    prompt = "Recreate this image with slight variations while maintaining the core composition and style"

    try:
        # Load the image
        image = PIL.Image.open(image_path)
        
        # Use the Gemini model that supports image generation
        model = genai.GenerativeModel("gemini-2.0-flash-preview-image-generation")
        
        response = model.generate_content([prompt, image])
        
        # Check if response has image data
        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'content') and candidate.content.parts:
                for part in candidate.content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        # Save the generated image
                        new_image_path = f"outputs/variation_{iteration}.png"
                        with open(new_image_path, "wb") as f:
                            f.write(part.inline_data.data)
                        return new_image_path
        
        # If no image data found, check for text response
        if response.text:
            print(f"Model response: {response.text}")
            raise Exception("Model did not generate an image, only text response.")
        else:
            raise Exception("Image generation failed. No image data in response.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Generate image variations using Google's Gemini 2.0 Flash Preview Image Generation model."
    )
    parser.add_argument("image_path", type=str, help="The path to the initial image.")
    parser.add_argument("count", type=int, help="The number of variations to generate.")
    args = parser.parse_args()

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    current_image_path = args.image_path
    for i in range(args.count):
        current_image_path = generate_image_variation(current_image_path, i + 1)
        print(f"Saved new image to {current_image_path}")


if __name__ == "__main__":
    main()
