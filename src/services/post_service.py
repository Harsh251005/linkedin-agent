from openai import OpenAI

from src.prompts.linkedin_writer import LINKEDIN_SYSTEM_PROMPT
from src.state.draft_state import draft_state
from src.config.settings import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class PostService:

    @staticmethod
    def create_post(topic: str) -> str:

        response = client.responses.create(
            model="gpt-5-nano",
            instructions=LINKEDIN_SYSTEM_PROMPT,
            input=f"Create a LinkedIn post about: {topic}"
        )

        draft_state.current_draft = response.output_text

        return response.output_text

    @staticmethod
    def rewrite_post(instruction: str) -> str:

        if not draft_state.current_draft:
            return "No active draft found."

        response = client.responses.create(
            model="gpt-5-mini",
            instructions=LINKEDIN_SYSTEM_PROMPT,
            input=f"""
Current Draft:

{draft_state.current_draft}

Instruction:
{instruction}

Rewrite the post accordingly.
"""
        )

        draft_state.current_draft = response.output_text

        return response.output_text