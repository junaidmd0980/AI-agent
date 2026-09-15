import os
import sys
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import call_function, available_functions


def generate_content(client, messages):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions,
    )
    return response


def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    parser = argparse.ArgumentParser(description="AI agent")
    parser.add_argument("user_prompt", type=str, help="Write a prompt for the AI agent")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(20):
        response = generate_content(client, messages)

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        message = response.choices[0].message

        messages.append(message)

        if not message.tool_calls:
            print(f"Final response:\n{message.content}")
            return

        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)

            if not result_message.get("content"):
                raise Exception("Error: Tool message content cannot be empty")

            messages.append(result_message)

            if args.verbose:
                print(f"-> {result_message['content']}")

    print("Error: Agent failed to complete the task")
    sys.exit(1)


if __name__ == "__main__":
    main()
