import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    env_api_key = os.environ.get("GEMINI_API_KEY")

    if not env_api_key:
        raise RuntimeError("Gemini API key not found")

    client = genai.Client(api_key=env_api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
