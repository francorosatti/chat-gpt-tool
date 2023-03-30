import credentials
import webbrowser

from clients.http_client import HttpClient
from gpt.image.image_generator import ImageGenerator, IMG_SIZE_BG, IMG_SIZE_MD, IMG_SIZE_SM
from gpt.text.text_generator import TextGenerator
from utils.arguments import parse_arguments, OPERATION_TEXT, OPERATION_IMAGE, SIZE_BG, SIZE_MD, SIZE_SM

client = HttpClient(credentials.OPEN_AI_URL, credentials.OPEN_AI_API_KEY)


def run_image(size, prompt):
    generator = ImageGenerator(client)

    if prompt is None:
        prompt = input("prompt: ")

    try:
        response = generator.generate_image(prompt, parse_size(size))
        img_url = response["data"][0]["url"]
        print(f"ChatGPT: Image url {img_url}")
        webbrowser.open(img_url, new=2)
    except Exception as e:
        print(f"couldn't generate image: {e}")


def parse_size(size):
    if size == SIZE_BG:
        return IMG_SIZE_BG
    if size == SIZE_MD:
        return IMG_SIZE_MD
    if size == SIZE_SM:
        return IMG_SIZE_SM


def run_text(continuous, prompt):
    generator = TextGenerator(client)
    generate_next_text(generator, continuous, prompt)


def generate_next_text(generator, continuous, prompt=None):
    if prompt is None:
        prompt = input("You: ")

    try:
        response = generator.create_completion(prompt)
        print(f"ChatGPT: {response['choices'][0]['message']['content']}")
    except Exception as e:
        print(f"couldn't create completion: {e}")

    if continuous:
        generate_next_text(generator, continuous)


if __name__ == "__main__":
    operation, size, continuous, prompt = parse_arguments()
    if operation == OPERATION_TEXT:
        run_text(continuous, prompt)
    elif operation == OPERATION_IMAGE:
        run_image(size, prompt)
    else:
        exit("unexpected operation")
