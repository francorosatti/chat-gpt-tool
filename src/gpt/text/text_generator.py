class TextGenerator:
    # Constants
    URL_CREATE_COMPLETION = "/chat/completions"

    MODEL_GPT_3_5_TURBO = "gpt-3.5-turbo"

    def __init__(self, http_client):
        self.client = http_client

    def create_completion(self, prompt: str):
        body = {
            "model": self.MODEL_GPT_3_5_TURBO,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}],
            "n": 1,
            "max_tokens": 50,
            "frequency_penalty": 1.0,
            "user": "test_user",
        }
        return self.client.post(self.URL_CREATE_COMPLETION, body)
