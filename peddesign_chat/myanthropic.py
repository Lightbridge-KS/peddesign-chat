import os
import anthropic

# Fetch the API key from environment variables
API_KEY = os.environ.get("ANTHROPIC_API_KEY")
MODEL_NAME = "claude-3-haiku-20240307"

# Initialize the Anthropomorphic client
client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str, system_prompt: str = "", prefill: str = "") -> str:
    """
    Get a completion from the Claude-3 model.

    :param prompt: The user's prompt to the model.
    :param system_prompt: The system prompt setting the context for the model.
    :param prefill: The prefill content to help guide the model's response.
    :return: The text of the model's completion.
    """
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prefill}
        ]
    )
    return message.content[0].text
