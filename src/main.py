import credentials
import webbrowser

from src.gpt.image.image_generator import ImageGenerator
from src.platform.http_client import HttpClient

client = HttpClient(credentials.OPEN_AI_URL, credentials.OPEN_AI_API_KEY)

generator = ImageGenerator(client)

prompt = input("Enter your prompt: ")

response = generator.generate_image(prompt)

try:
    img_url = response["data"][0]["url"]
    webbrowser.open(img_url, new=2)
except Exception as e:
    print(f"couldn't generate image {e}")
