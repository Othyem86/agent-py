import os
import argparse
from argparse import Namespace
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import MODEL_NAME, SYSTEM_PROMPT, TEMPERATURE
from call_function import available_functions, call_function

def main() -> None:
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()    
    
    messages = [
        types.Content(
            role="user", 
            parts=[
                types.Part(text=args.user_prompt)
            ]
        )
    ]
    client = get_genai_client()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=messages,
        config=types.GenerateContentConfig(
            temperature=TEMPERATURE,
            tools=[available_functions], 
            system_instruction=SYSTEM_PROMPT
        )
    )
    print_prompt_output(args, response)


def get_genai_client() -> genai.Client:
    load_dotenv()
    env_api_key = os.environ.get("GEMINI_API_KEY")

    if not env_api_key:
        raise RuntimeError("Gemini API key not found")

    return genai.Client(api_key=env_api_key)


def print_prompt_output(args: Namespace, response: genai.Client) -> None:
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print()

    if not response.function_calls:
        print("Response:")
        print(response.text)

    function_results = []
    for f in response.function_calls:
        function_call_result = call_function(f, args.verbose)

        if not function_call_result.parts or len(function_call_result.parts) == 0:
            raise Exception(f"Error: Parts list in call function call result is empty")
        if not function_call_result.parts[0].function_response:
            raise Exception(f"Error: Invalid function response in call function call result")
        if not function_call_result.parts[0].function_response.response:
            raise Exception(f"Error: Invalid response in function response")
        
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_results.append(function_call_result.parts[0])
        

if __name__ == "__main__":
    main()
