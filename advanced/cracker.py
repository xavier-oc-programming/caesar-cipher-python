from cipher import CaesarCipher, CipherMode
from config import ALPHABET, ENGLISH_FREQ


class CipherCracker:
    """Cryptanalysis tools for Caesar-encrypted text."""

    def __init__(self) -> None:
        self._cipher = CaesarCipher()

    def brute_force(self, text: str) -> list[tuple[int, str]]:
        """Return all 26 possible decryptions as (shift, decrypted_text) pairs."""
        return [
            (shift, self._cipher.run(text, shift, CipherMode.DECODE))
            for shift in range(len(ALPHABET))
        ]

    def frequency_analysis(self, text: str) -> tuple[int, str, float]:
        """
        Auto-detect the shift using English letter frequency scoring.
        Returns (best_shift, decrypted_text, confidence_score).
        Higher score = closer match to expected English frequencies.
        """
        letters_only = [c for c in text.lower() if c in ALPHABET]
        if not letters_only:
            return 0, text, 0.0

        best_shift = 0
        best_score = float("-inf")

        for shift in range(len(ALPHABET)):
            decrypted = self._cipher.run(text, shift, CipherMode.DECODE)
            score = self._score_text(decrypted)
            if score > best_score:
                best_score = score
                best_shift = shift

        best_decrypted = self._cipher.run(text, best_shift, CipherMode.DECODE)
        return best_shift, best_decrypted, best_score

    def _score_text(self, text: str) -> float:
        """
        Score a string by comparing its letter frequencies to expected English.
        Uses sum of squared errors — lower divergence = higher score.
        """
        letters = [c for c in text.lower() if c in ALPHABET]
        if not letters:
            return float("-inf")

        total = len(letters)
        freq: dict[str, int] = {}
        for char in letters:
            freq[char] = freq.get(char, 0) + 1

        score = 0.0
        for char, count in freq.items():
            observed = (count / total) * 100
            expected = ENGLISH_FREQ.get(char, 0.0)
            score -= (observed - expected) ** 2

        return score
