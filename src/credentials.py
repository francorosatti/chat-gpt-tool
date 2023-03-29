import os
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_URL = os.getenv('OPEN_AI_URL')
OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')
