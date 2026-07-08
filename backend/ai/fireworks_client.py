import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1",
)


class FireworksClient:

    def chat(self, system_prompt: str, user_prompt: str) -> str:

        response = client.chat.completions.create(
            model=os.getenv("FIREWORKS_MODEL"),
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            temperature=0.1,
            
        )

        return response.choices[0].message.content