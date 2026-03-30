from pathlib import Path

from cipher import CaesarCipher, CipherMode


class FileHandler:
    """Encrypt or decrypt plain-text files using the Caesar cipher."""

    def __init__(self) -> None:
        self._cipher = CaesarCipher()

    def process(self, input_path: str, output_path: str, shift: int, mode: CipherMode) -> None:
        source = Path(input_path)
        if not source.exists():
            raise FileNotFoundError(f"No file found at '{input_path}'")
        if source.suffix.lower() != ".txt":
            raise ValueError("Only .txt files are supported.")

        text = source.read_text(encoding="utf-8")
        result = self._cipher.run(text, shift, mode)
        Path(output_path).write_text(result, encoding="utf-8")
