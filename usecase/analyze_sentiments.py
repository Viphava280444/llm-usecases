from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv('OPENROUTER_ENDPOINT'),
    api_key=os.getenv('API_KEY')
)

def analyze_sentiment(text):

    model = "google/gemma-3-27b-it:free"
    message = [
        {"role": "user", "content": f"Analyze the sentiment of the following text: \"{text}\". Is it positive, negative, or neutral? Answer in one word with no punctuation."}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=message
    )
    return response.choices[0].message.content.strip().lower()

print(analyze_sentiment('This is very bad'))
    