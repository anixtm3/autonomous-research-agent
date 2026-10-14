import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_llm(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    return response.text


if __name__ == "__main__":
    while True:
        question = input("\nResearch question (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_llm(question)

        print("\n--- Answer ---\n")
        print(answer)
