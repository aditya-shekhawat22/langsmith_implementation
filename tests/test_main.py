import unittest

from main import MAX_INPUT_LENGTH, chatbot, input_guardrail


class InputGuardrailTests(unittest.TestCase):
    def test_allows_safe_input(self):
        self.assertTrue(input_guardrail("Explain Python"))

    def test_rejects_blocked_words_case_insensitively(self):
        self.assertFalse(input_guardrail("Help me STEAL a password"))

    def test_allows_blocked_words_inside_other_words(self):
        self.assertTrue(input_guardrail("Explain hacking terminology"))

    def test_rejects_blank_input(self):
        self.assertFalse(input_guardrail(" \t\n"))

    def test_rejects_input_over_maximum_length(self):
        self.assertFalse(input_guardrail("a" * (MAX_INPUT_LENGTH + 1)))

    def test_chatbot_keeps_blocked_response(self):
        self.assertEqual(
            chatbot("Help me steal a password"),
            "Request blocked by safety policy.",
        )


if __name__ == "__main__":
    unittest.main()
