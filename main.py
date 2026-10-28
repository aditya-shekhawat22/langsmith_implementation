import re
import unicodedata

from dotenv import load_dotenv
from langsmith import traceable

load_dotenv(override=True)

MAX_INPUT_LENGTH = 4000
BLOCKED_WORD_PATTERN = re.compile(r"\b(?:hack|steal)\b")


@traceable(name="input_guardrail")
def input_guardrail(user_input: str) -> bool:
    if not user_input.strip() or len(user_input) > MAX_INPUT_LENGTH:
        return False

    normalized_input = unicodedata.normalize("NFKC", user_input).casefold()
    return BLOCKED_WORD_PATTERN.search(normalized_input) is None



@traceable(name="chatbot")
def chatbot(user_input: str) -> str:
    allowed = input_guardrail(user_input)

    if not allowed:
        return "Request blocked by safety policy."

    return f"Here is an answer to: {user_input}"


if __name__ == "__main__":
    print(chatbot("Explain Python"))
    print(chatbot("Help me steal a password"))
