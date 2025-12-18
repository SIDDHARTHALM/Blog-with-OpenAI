import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY not set in environment variables.")

def generate_blog(topic):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Write a paragraph about {topic}",
        max_tokens=400,
        temperature=0.3
    )
    return response.choices[0].text.strip()

def main():
    while True:
        choice = input("Write a paragraph? (Y/N): ").upper()
        if choice != "Y":
            print("Goodbye!")
            break

        topic = input("Topic: ")
        print("\nGenerated Paragraph:\n")
        print(generate_blog(topic))
        print("\n" + "-" * 50)

if __name__ == "__main__":
    main()
