from dataclasses import dataclass


@dataclass
class DraftState:
    current_draft: str | None = None


draft_state = DraftState()