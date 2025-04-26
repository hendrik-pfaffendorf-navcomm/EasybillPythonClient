from enum import Enum


class ProjectBudgetNotifyFrequency(str, Enum):
    ALWAYS = "ALWAYS"
    NEVER = "NEVER"
    ONCE = "ONCE"

    def __str__(self) -> str:
        return str(self.value)
