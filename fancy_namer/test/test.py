import unittest
from fancy_namer.namer import FancyNamer, load_word_list
from fancy_namer.enums import NameType
from fancy_namer.exceptions import InvalidToolNameError


class TestFancyNamer(unittest.TestCase):
    def test_standard_name_generation(self) -> None:
        fancy_namer = FancyNamer(name_type=NameType.STANDARD, random_seed=42)
        name = fancy_namer.generate_name()
        self.assertIsInstance(name, str)
        self.assertIn("_of_", name)

    def test_computer_science_name_generation(self) -> None:
        fancy_namer = FancyNamer(name_type=NameType.COMPUTER_SCIENCE, random_seed=42)
        name = fancy_namer.generate_name()
        self.assertIsInstance(name, str)
        self.assertIn("_of_", name)

    def test_tool_name_generation(self) -> None:
        tool_name = "MyTool"
        fancy_namer = FancyNamer(name_type=NameType.TOOL, tool_name=tool_name, random_seed=42)
        name = fancy_namer.generate_name()
        self.assertIsInstance(name, str)
        self.assertIn(tool_name, name)

    def test_tool_name_generation_without_tool_name(self) -> None:
        with self.assertRaises(InvalidToolNameError):
            FancyNamer(name_type=NameType.TOOL)

    def test_load_word_list(self) -> None:
        adjectives = load_word_list("adjectives.txt")
        nouns = load_word_list("nouns.txt")
        places = load_word_list("places.txt")
        computer_science_terms = load_word_list("computer_science_terms.txt")
        
        self.assertGreater(len(adjectives), 0)
        self.assertGreater(len(nouns), 0)
        self.assertGreater(len(places), 0)
        self.assertGreater(len(computer_science_terms), 0)