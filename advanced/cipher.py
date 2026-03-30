from dataclasses import dataclass
from enum import Enum

from config import ALPHABET


class CipherMode(Enum):
    ENCODE = "encode"
    DECODE = "decode"


@dataclass
class CaesarCipher:
    """Shifts each letter in the text by a fixed number of positions."""

    def run(self, text: str, shift: int, mode: CipherMode) -> str:
        shift %= len(ALPHABET)
        if mode == CipherMode.DECODE:
            shift *= -1

        result = ""
        for char in text.lower():
            if char in ALPHABET:
                shifted = (ALPHABET.index(char) + shift) % len(ALPHABET)
                result += ALPHABET[shifted]
            else:
                result += char
        return result


@dataclass
class VigenereCipher:
    """Encrypts using a repeating keyword — each letter sets its own shift amount."""

    def run(self, text: str, keyword: str, mode: CipherMode) -> str:
        keyword = keyword.lower()
        result = ""
        key_index = 0

        for char in text.lower():
            if char in ALPHABET:
                key_shift = ALPHABET.index(keyword[key_index % len(keyword)])
                if mode == CipherMode.DECODE:
                    key_shift *= -1
                shifted = (ALPHABET.index(char) + key_shift) % len(ALPHABET)
                result += ALPHABET[shifted]
                key_index += 1
            else:
                result += char
        return result
