import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class Chatbot:
    def __init__(self):
        groq_api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=groq_api_key)

    def get_response(self, user_input):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Make a Skibidi Toilet script.")
    print(response)
