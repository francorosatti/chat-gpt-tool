IMG_SIZE_BG = "1024x1024"
IMG_SIZE_MD = "512x512"
IMG_SIZE_SM = "256x256"

class ImageGenerator:
    # Constants
    URL_GENERATE_IMAGE = "/images/generations"

    def __init__(self, http_client):
        self.client = http_client

    def generate_image(self, prompt: str, size: str):
        body = {
            "prompt": prompt,
            "n": 1,
            "size": size,
        }
        return self.client.post(self.URL_GENERATE_IMAGE, body)
