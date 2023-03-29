import credentials
import webbrowser

from gpt.image.image_generator import ImageGenerator
from platform.http_client import HttpClient


def run():
    client = HttpClient(credentials.OPEN_AI_URL, credentials.OPEN_AI_API_KEY)

    generator = ImageGenerator(client)

    prompt = input("Enter your prompt: ")
    print("Processing your prompt...")

    try:
        response = generator.generate_image(prompt)
        img_url = response["data"][0]["url"]
        print(f"Image {img_url} opened in browser")
        webbrowser.open(img_url, new=2)
    except Exception as e:
        print(f"couldn't generate image: {e}: response {response}")


if __name__ == "__main__":
    run()
