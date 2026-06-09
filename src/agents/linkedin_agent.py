from agents import Agent, function_tool
from src.prompts.linkedin_agent import LINKEDIN_AGENT_PROMPT

from src.services.post_service import PostService


@function_tool
def create_post(topic: str) -> str:
    return PostService.create_post(topic)


@function_tool
def edit_post(instruction: str) -> str:
    return PostService.rewrite_post(instruction)


linkedin_agent = Agent(
    name="LinkedIn Agent",
    instructions=LINKEDIN_AGENT_PROMPT,
    tools=[
        create_post,
        edit_post
    ]
)