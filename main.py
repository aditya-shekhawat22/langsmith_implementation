
from dotenv import load_dotenv
from langsmith import traceable

load_dotenv(override=True)


@traceable(name="input_guardrail")
def input_guardrail(user_input: str) -> bool:
    blocked_words = ["hack", "steal"]

    for word in blocked_words:
        if word in user_input.lower():
            return False

    return True


@traceable(name="chatbot")
def chatbot(user_input: str) -> str:
    allowed = input_guardrail(user_input)

    if not allowed:
        return "Request blocked by safety policy."

    return f"Here is an answer to: {user_input}"


if __name__ == "__main__":
    print(chatbot("Explain Python"))
    print(chatbot("Help me steal a password"))
