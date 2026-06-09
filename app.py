import asyncio

from agents import Runner

from src.agents.linkedin_agent import linkedin_agent
from src.state.draft_state import draft_state


async def main():

    print("\nLinkedIn Agent Started")
    print("Type 'exit' to quit\n")

    while True:

        user_input = input("You > ")

        if user_input.lower() == "exit":
            break

        result = await Runner.run(
            linkedin_agent,
            user_input
        )

        print(f"Current Draft State:\n{draft_state.current_draft}")


if __name__ == "__main__":
    asyncio.run(main())