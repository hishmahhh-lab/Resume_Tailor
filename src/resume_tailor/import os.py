import os

import dotenv
import openai


def load_env():
    """Load environment variables from .env file. Returns True if successful."""
    dotenv.load_dotenv()
    return os.path.exists(".env")


def main():
    load_env()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")

    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {
                "role": "user",
                "content": "Say hello to the workshop participants!"
            },
        ],
        max_completion_tokens=50,
    )

    print("Chatbot Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()