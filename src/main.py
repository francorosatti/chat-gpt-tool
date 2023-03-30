import credentials
import webbrowser

from gpt.image.image_generator import ImageGenerator
from clients.http_client import HttpClient
from src.gpt.text.text_generator import TextGenerator

client = HttpClient(credentials.OPEN_AI_URL, credentials.OPEN_AI_API_KEY)


def run_image():
    generator = ImageGenerator(client)

    prompt = input("Enter your prompt: ")
    print("Processing your prompt...")

    try:
        response = generator.generate_image(prompt)
        img_url = response["data"][0]["url"]
        print(f"Image {img_url} opened in browser")
        webbrowser.open(img_url, new=2)
    except Exception as e:
        print(f"couldn't generate image: {e}")


def run_text():
    generator = TextGenerator(client)

    prompt = input("Enter your prompt: ")
    print("Processing your prompt...")

    try:
        response = generator.create_completion(prompt)
        print(f"Chat GPT says: {response['choices'][0]['message']['content']}")
    except Exception as e:
        print(f"couldn't create completion: {e}")


if __name__ == "__main__":
    run_text()
