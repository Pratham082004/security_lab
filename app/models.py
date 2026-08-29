"""Application models."""

from dataclasses import dataclass


@dataclass
class BaseModel:
    """Simple base model for application entities."""
    id: int | None = None


def create_model() -> BaseModel:
    """Create a simple model instance."""
    return BaseModel()


if __name__ == '__main__':
    print(create_model())
