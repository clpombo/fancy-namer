import random
from typing import Optional
from pathlib import Path

from exceptions import InvalidToolNameError
from enums import NameType


def load_word_list(filename: str) -> list[str]:
    path = (Path(__file__).parent / "data" / filename)
    with path.open() as f:
        word_list = []
        for line in f:
            word_list.extend([word for word in line.strip().split()])
    return word_list

class FancyNamer:
    def __init__(
        self,
        name_type: NameType = NameType.STANDARD,
        tool_name: Optional[str] = None,
        random_seed: Optional[int] = None,
    ) -> None:
        self.random_seed = random_seed
        self.random_gen = random.Random(random_seed)
        self.name_type = name_type
        self.tool_name = tool_name
        if (self.name_type == NameType.TOOL and not self.tool_name):
            raise InvalidToolNameError("tool_name must be provided when using NameType.TOOL")
        self.adjectives = load_word_list("adjectives.txt")
        match self.name_type:
            case NameType.STANDARD:
                self.nouns = load_word_list("nouns.txt")
            case NameType.COMPUTER_SCIENCE:
                self.nouns = load_word_list("computer_science_terms.txt")
            case NameType.TOOL:
                self.nouns = [self.tool_name]  # For TOOL type, the noun is just the tool name
            case _:
                raise InvalidToolNameError(f"Unsupported name type: {self.name_type}")
        self.places = load_word_list("places.txt")

    def generate_name(self) -> str:
        adjective = self.random_gen.choice(self.adjectives)
        noun = self.random_gen.choice(self.nouns)
        place = self.random_gen.choice(self.places)
        return f"{adjective}_{noun}_of_{place}"
    