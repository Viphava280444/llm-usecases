from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv('OPENROUTER_ENDPOINT'),
    api_key=os.getenv('API_KEY')
)

user_qestions = [
    "What's a popular choice for a first programming language?",
    "What are some advantages of learning it as my first language?",
    "Can you show me a simple 'Hello World' program written in that language?",
]

def simple_chatbot(questions):
    messages = [
            {
        "role": "system",
        "content": "You are a programming expert. Answer questions about programming languages"
    },
    ]

    for question in questions:
        message = {"role": "user", "content": question}
        messages.append(message)

        respond = client.chat.completions.create(
            model="google/gemma-3-27b-it:free",
            messages=messages
        )
        assistant_message = {"role": "assistant", "content": respond.choices[0].message.content}
        messages.append(assistant_message)

        print("Assistant: ", respond.choices[0].message.content, "\n")

simple_chatbot(user_qestions)




