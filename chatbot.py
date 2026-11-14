from google import genai
from dotenv import load_dotenv
import os

# API Key load
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Connect to Gemini AI
client = genai.Client(api_key=api_key)

# Create Chat
chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

print("Welcome to My AI Chatbot!")
print("Natho Telugu or English lo matladachu")
print("Stop cheyali ante bye type cheyyi")

while True:

    user_message = input("You: ")

    if user_message.lower() == "bye":
        print("Bot: Bye! See you again.")
        break

    try:
        response = chat.send_message(
            "Reply in the same language as the user. "
            "Use simple Telugu or English."
            + user_message
        )

        print("Bot:", response.text)

    except Exception as e:
        print("Error:", e)