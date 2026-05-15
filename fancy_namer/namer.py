from fileinput import filename
import random
from typing import Optional
from pathlib import Path

from exceptions import InvalidToolNameError
from enums import NameType


class FancyNamer:
    @staticmethod
    def generate_name(
            name_type: NameType = NameType.STANDARD,
            tool_name: Optional[str] = None,
            random_seed: Optional[int] = None
        ) -> str:
        if (name_type == NameType.TOOL and not tool_name):
            raise InvalidToolNameError("tool_name must be provided when using NameType.TOOL")
        adjectives = FancyNamer.load_word_list("adjectives.txt")
        match name_type:
            case NameType.STANDARD:
                nouns = FancyNamer.load_word_list("nouns.txt")
            case NameType.COMPUTER_SCIENCE:
                nouns = FancyNamer.load_word_list("computer_science_terms.txt")
            case NameType.TOOL:
                nouns = [tool_name]  # For TOOL type, the noun is just the tool name
            case _:
                raise InvalidToolNameError(f"Unsupported name type: {self.name_type}")
        places = FancyNamer.load_word_list("places.txt")
        random_gen = random.Random(random_seed)
        adjective = random_gen.choice(adjectives)
        noun = random_gen.choice(nouns)
        place = random_gen.choice(places)
        return f"{adjective}_{noun}_of_{place}"
    
    @staticmethod
    def load_word_list(filename: str) -> list[str]:
        path = (Path(__file__).parent / "data" / filename)
        with path.open() as f:
            word_list = []
            for line in f:
                word_list.extend([word for word in line.strip().split()])
        return word_list

