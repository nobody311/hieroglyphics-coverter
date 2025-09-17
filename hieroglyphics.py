"""
English to Egyptian Hieroglyphics Converter
===========================================

A comprehensive Python program that converts English text directly to Egyptian hieroglyphics
using Unicode Egyptian Hieroglyph characters based on the ancient Egyptian uniliteral alphabet.

Features:
- Convert English letters to corresponding hieroglyphic symbols
- Handle numbers using Egyptian numeral system
- Support for basic punctuation
- Detailed character-by-character conversion explanations
- Interactive user interface
- Batch conversion capabilities

Author: AI Assistant
Date: 2025
Based on: Gardiner's Egyptian Hieroglyphic Sign List and Unicode Egyptian Hieroglyphs standard
"""

import re
from typing import List, Tuple, Union, Dict


class HieroglyphicsConverter:
    """
    A comprehensive converter class for English to Egyptian hieroglyphics conversion.

    This converter uses the basic uniliteral (single consonant) hieroglyphic signs
    that correspond roughly to the English alphabet. The mapping is based on scholarly
    sources including Gardiner's sign list and Unicode Egyptian Hieroglyphs standard.

    Note: Ancient Egyptian hieroglyphs are far more complex than this simplified
    phonetic mapping suggests. Real hieroglyphic writing includes:
    - Logograms (word signs)
    - Phonograms (sound signs) 
    - Determinatives (meaning clarifiers)
    - Complex spatial arrangements
    """

    def __init__(self):
        """Initialize the converter with hieroglyphic mappings."""

        # Primary hieroglyphic alphabet mapping using Unicode Egyptian Hieroglyphs
        # Based on the 24 uniliteral signs that roughly correspond to alphabet letters
        self.hieroglyphic_map = {
            'a': '𓄿',  # U+1313F - Egyptian Hieroglyph AA001 (vulture) - aleph sound
            'b': '𓃀',  # U+130C0 - Egyptian Hieroglyph D058 (foot/leg) - 'b' sound  
            'c': '𓎡',  # U+133A1 - Egyptian Hieroglyph V031 (basket) - 'k/c' sound
            'd': '𓂧',  # U+130A7 - Egyptian Hieroglyph D046 (hand) - 'd' sound
            'e': '𓇋',  # U+131CB - Egyptian Hieroglyph M17 (reed) - 'i/e' vowel sound
            'f': '𓆑',  # U+13191 - Egyptian Hieroglyph I009 (horned viper) - 'f' sound
            'g': '𓎼',  # U+133BC - Egyptian Hieroglyph W011 (jar stand) - 'g' sound
            'h': '𓉔',  # U+13254 - Egyptian Hieroglyph O004 (shelter) - 'h' sound
            'i': '𓇋',  # U+131CB - Egyptian Hieroglyph M17 (reed) - 'i' vowel sound
            'j': '𓆳',  # U+131B3 - Egyptian Hieroglyph G043 (quail chick) - 'j' sound
            'k': '𓎡',  # U+133A1 - Egyptian Hieroglyph V031 (basket) - 'k' sound
            'l': '𓃭',  # U+130ED - Egyptian Hieroglyph E023 (lion) - 'l' sound
            'm': '𓅓',  # U+13153 - Egyptian Hieroglyph G017 (owl) - 'm' sound
            'n': '𓈖',  # U+13216 - Egyptian Hieroglyph N35 (water ripple) - 'n' sound
            'o': '𓅱',  # U+13171 - Egyptian Hieroglyph G043 (quail chick) - 'o/w' sound
            'p': '𓊪',  # U+132AA - Egyptian Hieroglyph Q003 (stool) - 'p' sound
            'q': '𓄿',  # U+1313F - Using vulture for 'q' (no direct ancient equivalent)
            'r': '𓂋',  # U+1308B - Egyptian Hieroglyph D021 (mouth) - 'r' sound
            's': '𓋴',  # U+132F4 - Egyptian Hieroglyph S029 (folded cloth) - 's' sound
            't': '𓏏',  # U+133CF - Egyptian Hieroglyph X001 (bread loaf) - 't' sound
            'u': '𓅱',  # U+13171 - Egyptian Hieroglyph G043 (quail chick) - 'u/w' sound
            'v': '𓆑',  # U+13191 - Egyptian Hieroglyph I009 (horned viper) - same as 'f'
            'w': '𓅱',  # U+13171 - Egyptian Hieroglyph G043 (quail chick) - 'w' sound
            'x': '𓎡',  # U+133A1 - Egyptian Hieroglyph V031 (basket) - using 'k' for 'x'
            'y': '𓇌',  # U+131CC - Egyptian Hieroglyph M17A (double reed) - 'y' sound
            'z': '𓊃',  # U+13283 - Egyptian Hieroglyph O034 (door bolt) - 'z' sound
        }

        # Special characters and punctuation
        self.special_chars = {
            ' ': ' ',    # Space remains space (word separator)
            '.': '𓏤',   # U+133E4 - Egyptian Hieroglyph Z001 (stroke) - sentence end
            ',': '𓏤',   # Using stroke for comma
            '!': '𓏤',   # Using stroke for exclamation
            '?': '𓏤',   # Using stroke for question mark
            ':': '𓏤',   # Using stroke for colon
            ';': '𓏤',   # Using stroke for semicolon
            '-': '𓏤',   # Using stroke for hyphen
            "'": '',    # Apostrophe ignored (not used in ancient Egyptian)
            '"': '',    # Quotation marks ignored
        }

        # Egyptian number system (simplified representation)
        # Ancient Egyptians used a decimal system with specific symbols
        self.numbers = {
            '0': '𓍢',   # Modern concept of zero (not in ancient Egyptian)
            '1': '𓏺',   # U+133FA - Egyptian Hieroglyph Z002 (single stroke)
            '2': '𓏻',   # U+133FB - Egyptian Hieroglyph Z003 (two strokes)
            '3': '𓏼',   # U+133FC - Egyptian Hieroglyph Z004 (three strokes)
            '4': '𓏽',   # U+133FD - Egyptian Hieroglyph Z005 (four strokes)
            '5': '𓏾',   # U+133FE - Egyptian Hieroglyph Z006 (five strokes)
            '6': '𓏿',   # U+133FF - Egyptian Hieroglyph Z007 (six strokes)
            '7': '𓐀',   # U+13400 - Egyptian Hieroglyph Z008 (seven strokes)
            '8': '𓐁',   # U+13401 - Egyptian Hieroglyph Z009 (eight strokes)
            '9': '𓐂',   # U+13402 - Egyptian Hieroglyph Z010 (nine strokes)
        }

        # Symbol descriptions for educational purposes
        self.symbol_descriptions = {
            '𓄿': 'Vulture (Aleph)',
            '𓃀': 'Foot/Leg',
            '𓎡': 'Basket',
            '𓂧': 'Hand',
            '𓇋': 'Reed',
            '𓆑': 'Horned Viper',
            '𓎼': 'Jar Stand',
            '𓉔': 'Shelter/House',
            '𓆳': 'Quail Chick',
            '𓃭': 'Lion',
            '𓅓': 'Owl',
            '𓈖': 'Water Ripple',
            '𓅱': 'Quail Chick',
            '𓊪': 'Stool',
            '𓂋': 'Mouth',
            '𓋴': 'Folded Cloth',
            '𓏏': 'Bread Loaf',
            '𓇌': 'Double Reed',
            '𓊃': 'Door Bolt',
            '𓏤': 'Stroke (separator)',
        }

    def convert_to_hieroglyphics(self, text: str) -> str:
        """
        Convert English text to Egyptian hieroglyphics.

        Args:
            text (str): The English text to convert

        Returns:
            str: The text converted to hieroglyphic symbols

        Raises:
            ValueError: If input is not a string
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string")

        if not text.strip():
            return ""

        # Convert to lowercase for consistent mapping
        text = text.lower()

        # Convert each character
        hieroglyphic_text = ""

        for char in text:
            if char in self.hieroglyphic_map:
                hieroglyphic_text += self.hieroglyphic_map[char]
            elif char in self.special_chars:
                hieroglyphic_text += self.special_chars[char]
            elif char in self.numbers:
                hieroglyphic_text += self.numbers[char]
            elif char.isspace():
                hieroglyphic_text += ' '
            else:
                # For unsupported characters, use stroke placeholder
                hieroglyphic_text += '𓏤'

        return hieroglyphic_text

    def convert_with_explanation(self, text: str) -> Tuple[str, List[str]]:
        """
        Convert text and provide detailed character-by-character explanation.

        Args:
            text (str): The English text to convert

        Returns:
            tuple: (hieroglyphic_text, list_of_explanations)

        Raises:
            ValueError: If input is not a string
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string")

        if not text.strip():
            return "", []

        text = text.lower()
        hieroglyphic_text = ""
        explanations = []

        for char in text:
            if char in self.hieroglyphic_map:
                hieroglyph = self.hieroglyphic_map[char]
                description = self.symbol_descriptions.get(hieroglyph, "Unknown symbol")
                hieroglyphic_text += hieroglyph
                explanations.append(f"'{char}' → {hieroglyph} ({description})")
            elif char in self.special_chars:
                hieroglyph = self.special_chars[char]
                hieroglyphic_text += hieroglyph
                explanations.append(f"'{char}' → {hieroglyph} (punctuation)")
            elif char in self.numbers:
                hieroglyph = self.numbers[char]
                hieroglyphic_text += hieroglyph
                explanations.append(f"'{char}' → {hieroglyph} (Egyptian numeral)")
            elif char.isspace():
                hieroglyphic_text += ' '
                explanations.append(f"[space] → [space] (word separator)")
            else:
                hieroglyphic_text += '𓏤'
                explanations.append(f"'{char}' → 𓏤 (unsupported → stroke placeholder)")

        return hieroglyphic_text, explanations

    def get_character_info(self, char: str) -> str:
        """
        Get detailed information about a character's hieroglyphic representation.

        Args:
            char (str): Single character to look up

        Returns:
            str: Detailed information about the character's conversion
        """
        if len(char) != 1:
            return "Please provide a single character"

        char = char.lower()

        if char in self.hieroglyphic_map:
            hieroglyph = self.hieroglyphic_map[char]
            description = self.symbol_descriptions.get(hieroglyph, "Unknown symbol")
            return f"'{char}' → {hieroglyph} ({description}) - Egyptian hieroglyphic letter"
        elif char in self.special_chars:
            hieroglyph = self.special_chars[char]
            return f"'{char}' → {hieroglyph} (special character/punctuation)"
        elif char in self.numbers:
            hieroglyph = self.numbers[char]
            return f"'{char}' → {hieroglyph} (Egyptian numeral)"
        elif char.isspace():
            return f"'{char}' → [space] (word separator)"
        else:
            return f"'{char}' is not supported and will be replaced with 𓏤 (stroke placeholder)"

    def batch_convert(self, text_list: List[str]) -> List[str]:
        """
        Convert multiple texts to hieroglyphics.

        Args:
            text_list (list): List of strings to convert

        Returns:
            list: List of converted hieroglyphic strings
        """
        return [self.convert_to_hieroglyphics(text) for text in text_list]

    def get_alphabet_reference(self) -> Dict[str, str]:
        """
        Get a complete reference of the alphabet mapping.

        Returns:
            dict: Dictionary mapping letters to hieroglyphs with descriptions
        """
        reference = {}
        for letter, hieroglyph in self.hieroglyphic_map.items():
            description = self.symbol_descriptions.get(hieroglyph, "Unknown")
            reference[letter] = f"{hieroglyph} ({description})"
        return reference

    def validate_text(self, text: str) -> Tuple[bool, List[str]]:
        """
        Validate input text and identify unsupported characters.

        Args:
            text (str): Text to validate

        Returns:
            tuple: (is_fully_supported, list_of_unsupported_chars)
        """
        unsupported = []
        all_supported_chars = (
            set(self.hieroglyphic_map.keys()) |
            set(self.special_chars.keys()) |
            set(self.numbers.keys()) |
            {' ', '\t', '\n'}
        )

        for char in text.lower():
            if char not in all_supported_chars and char not in unsupported:
                unsupported.append(char)

        return len(unsupported) == 0, unsupported


def interactive_converter():
    """
    Interactive command-line interface for the hieroglyphics converter.
    """
    converter = HieroglyphicsConverter()

    print("="*70)
    print("🔺 ENGLISH TO EGYPTIAN HIEROGLYPHICS CONVERTER 🔺")
    print("="*70)
    print("Welcome! This tool converts English text to Egyptian hieroglyphics")
    print("using the ancient Egyptian uniliteral alphabet.")
    print()
    print("Commands:")
    print("  'help' - Show this help message")
    print("  'alphabet' - Display the full alphabet reference")
    print("  'examples' - Show conversion examples")
    print("  'quit' or 'exit' - Exit the program")
    print("  Any other text - Convert to hieroglyphics")
    print()

    while True:
        try:
            user_input = input("Enter text to convert (or command): ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Thank you for using the Hieroglyphics Converter! 𓋹")
                break

            elif user_input.lower() == 'help':
                print("\nHELP:")
                print("This converter translates English letters to Egyptian hieroglyphic")
                print("symbols based on the ancient uniliteral alphabet. Each English")
                print("letter corresponds to a hieroglyphic sign that represents a")
                print("similar sound. Numbers 0-9 are converted to Egyptian numerals.")
                print()

            elif user_input.lower() == 'alphabet':
                print("\nHIEROGLYPHIC ALPHABET REFERENCE:")
                print("-" * 50)
                reference = converter.get_alphabet_reference()
                for letter in sorted(reference.keys()):
                    print(f"{letter.upper()}: {reference[letter]}")
                print()

            elif user_input.lower() == 'examples':
                print("\nCONVERSION EXAMPLES:")
                print("-" * 30)
                examples = [
                    "hello", "egypt", "pyramid", "pharaoh", 
                    "nile", "ancient", "hieroglyph", "123"
                ]
                for example in examples:
                    converted = converter.convert_to_hieroglyphics(example)
                    print(f"{example:12} → {converted}")
                print()

            else:
                # Convert the input
                print("\nCONVERSION RESULT:")
                print("-" * 30)

                # Check for unsupported characters
                is_supported, unsupported = converter.validate_text(user_input)
                if not is_supported:
                    print(f"⚠️  Warning: Unsupported characters found: {unsupported}")
                    print("These will be replaced with 𓏤 (stroke placeholder)")
                    print()

                # Perform conversion with explanation
                hieroglyphic, explanations = converter.convert_with_explanation(user_input)

                print(f"Original:     {user_input}")
                print(f"Hieroglyphic: {hieroglyphic}")
                print()

                # Show detailed breakdown for shorter texts
                if len(user_input) <= 20:
                    print("Character breakdown:")
                    for explanation in explanations:
                        print(f"  {explanation}")
                    print()

        except KeyboardInterrupt:
            print("\n\nExiting... 𓋹")
            break
        except Exception as e:
            print(f"Error: {e}")


def demo_converter():
    """
    Demonstration function showing various features of the converter.
    """
    print("="*70)
    print("🔺 HIEROGLYPHICS CONVERTER DEMONSTRATION 🔺")
    print("="*70)
    print()

    converter = HieroglyphicsConverter()

    # Basic conversion examples
    print("1. BASIC CONVERSIONS:")
    print("-" * 30)

    demo_texts = [
        "hello world",
        "ancient egypt", 
        "pyramid power",
        "pharaoh king",
        "nile river",
        "hieroglyphics rock",
        "amazing discovery 123"
    ]

    for text in demo_texts:
        converted = converter.convert_to_hieroglyphics(text)
        print(f"{text:20} → {converted}")

    print()

    # Detailed explanation example
    print("2. DETAILED CONVERSION BREAKDOWN:")
    print("-" * 40)

    sample = "egypt"
    hieroglyphic, explanations = converter.convert_with_explanation(sample)
    print(f"Converting: '{sample}'")
    print(f"Result: {hieroglyphic}")
    print("\nBreakdown:")
    for explanation in explanations:
        print(f"  {explanation}")

    print()

    # Alphabet display
    print("3. HIEROGLYPHIC ALPHABET:")
    print("-" * 35)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i, letter in enumerate(alphabet):
        hieroglyph = converter.hieroglyphic_map[letter]
        description = converter.symbol_descriptions.get(hieroglyph, "")
        print(f"{letter.upper()}: {hieroglyph} ({description})")

        # Print in columns of 13
        if i == 12:
            print()

    print()

    # Numbers demonstration
    print("4. EGYPTIAN NUMERALS:")
    print("-" * 25)

    for digit in "0123456789":
        hieroglyph = converter.numbers[digit]
        print(f"{digit}: {hieroglyph}")

    print()
    print("="*70)


if __name__ == "__main__":
    """
    Main execution block - choose between demo and interactive mode
    """
    print("Choose mode:")
    print("1. Interactive Converter")
    print("2. Demo/Examples")
    print("3. Both")

    try:
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            interactive_converter()
        elif choice == "2":
            demo_converter()
        elif choice == "3":
            demo_converter()
            print("\n")
            interactive_converter()
        else:
            print("Running demo by default...")
            demo_converter()

    except KeyboardInterrupt:
        print("\nGoodbye! 𓋹")
    except Exception as e:
        print(f"Error: {e}")
