import sys
import os

# Allow imports from this directory when launched via subprocess
sys.path.insert(0, os.path.dirname(__file__))

from cipher import CaesarCipher, VigenereCipher, CipherMode
from cracker import CipherCracker
from file_io import FileHandler
import display


def caesar_mode() -> None:
    display.clear()
    display.divider()
    print(f"\n  {display.Colors.CYAN}Caesar Cipher{display.Colors.RESET}\n")
    print(f"  {display.Colors.DIM}Each letter in your message is shifted a fixed number of positions")
    print(f"  along the alphabet. Shift 3 turns A→D, B→E, Z→C, and so on.")
    print(f"  Non-letters (spaces, numbers, punctuation) are left unchanged.{display.Colors.RESET}\n")
    direction = input("  encode or decode? ").strip().lower()
    if direction not in ("encode", "decode"):
        display.print_error("Please type 'encode' or 'decode'.")
        return
    text = input("  Enter your message: ").strip()
    shift = _get_shift()
    if shift is None:
        return

    mode = CipherMode.ENCODE if direction == "encode" else CipherMode.DECODE
    result = CaesarCipher().run(text, shift, mode)
    display.print_result(direction, text, result)


def vigenere_mode() -> None:
    display.clear()
    display.divider()
    print(f"\n  {display.Colors.CYAN}Vigenère Cipher{display.Colors.RESET}\n")
    print(f"  {display.Colors.DIM}A stronger version of Caesar — instead of one fixed shift, a keyword")
    print(f"  sets a different shift for each letter. The keyword repeats across")
    print(f"  your message, so 'KEY' shifts letters by 10, 4, 24 in rotation.")
    print(f"  This makes it far harder to crack than a single-shift cipher.{display.Colors.RESET}\n")
    direction = input("  encode or decode? ").strip().lower()
    if direction not in ("encode", "decode"):
        display.print_error("Please type 'encode' or 'decode'.")
        return
    text = input("  Enter your message: ").strip()
    keyword = input("  Enter keyword: ").strip()
    if not keyword.isalpha():
        display.print_error("Keyword must contain only letters.")
        return

    mode = CipherMode.ENCODE if direction == "encode" else CipherMode.DECODE
    result = VigenereCipher().run(text, keyword, mode)
    display.print_result(direction, text, result)


def brute_force_mode() -> None:
    display.clear()
    display.divider()
    print(f"\n  {display.Colors.CYAN}Brute Force{display.Colors.RESET}\n")
    print(f"  {display.Colors.DIM}Since Caesar only has 26 possible shifts, we can just try all of them.")
    print(f"  Every decryption is printed below — scan for the one that reads")
    print(f"  as real English and that's your answer. No keyword needed.{display.Colors.RESET}\n")
    text = input("  Enter the encrypted message: ").strip()
    results = CipherCracker().brute_force(text)
    display.print_brute_force(results)


def frequency_analysis_mode() -> None:
    display.clear()
    display.divider()
    print(f"\n  {display.Colors.CYAN}Frequency Analysis{display.Colors.RESET}\n")
    print(f"  {display.Colors.DIM}In English, some letters appear far more often than others —")
    print(f"  'e' is the most common, followed by 't', 'a', 'o', 'i', 'n', etc.")
    print(f"  This tool counts how often each letter appears in your ciphertext,")
    print(f"  then slides the frequency curve across all 26 shifts and scores each")
    print(f"  one against the expected English distribution.")
    print(f"  The shift with the closest match is returned as the most likely answer.")
    print(f"  Works best on longer messages — short texts may not have enough data.{display.Colors.RESET}\n")
    text = input("  Enter the encrypted message: ").strip()
    shift, decrypted, _ = CipherCracker().frequency_analysis(text)
    display.print_frequency_result(shift, decrypted, text)


def file_mode() -> None:
    display.clear()
    display.divider()
    print(f"\n  {display.Colors.CYAN}File Encrypt / Decrypt{display.Colors.RESET}\n")
    print(f"  {display.Colors.DIM}Encrypts or decrypts an entire .txt file using a Caesar shift.")
    print(f"  How to use:")
    print(f"    1. Save your message as a plain .txt file anywhere on your computer.")
    print(f"    2. Enter the full file path when prompted (e.g. /Users/you/message.txt).")
    print(f"    3. Enter a path for the output file (e.g. /Users/you/encrypted.txt).")
    print(f"    4. Choose a shift — use the same shift and opposite direction to decode.")
    print(f"  The output file will be created automatically if it doesn't exist.{display.Colors.RESET}\n")
    direction = input("  encode or decode? ").strip().lower()
    if direction not in ("encode", "decode"):
        display.print_error("Please type 'encode' or 'decode'.")
        return
    input_path = input("  Input file path (.txt): ").strip()
    if not input_path.endswith(".txt"):
        input_path += ".txt"
    output_path = input("  Output file path (.txt): ").strip()
    if not output_path.endswith(".txt"):
        output_path += ".txt"
    shift = _get_shift()
    if shift is None:
        return

    mode = CipherMode.ENCODE if direction == "encode" else CipherMode.DECODE
    try:
        FileHandler().process(input_path, output_path, shift, mode)
        display.print_file_result(direction, output_path)
    except (FileNotFoundError, ValueError) as e:
        display.print_error(str(e))


def _get_shift() -> int | None:
    try:
        return int(input("  Shift amount: ").strip())
    except ValueError:
        display.print_error("Shift must be a whole number.")
        return None


MENU = f"""
  {display.Colors.BOLD}Select a mode:{display.Colors.RESET}

  1  Caesar cipher       — encode / decode with a shift
  2  Vigenère cipher     — encode / decode with a keyword
  3  Brute force         — show all 26 possible decryptions
  4  Frequency analysis  — auto-detect the shift
  5  File encrypt/decrypt — encode or decode a .txt file
  6  Quit
"""

MODES = {
    "1": caesar_mode,
    "2": vigenere_mode,
    "3": brute_force_mode,
    "4": frequency_analysis_mode,
    "5": file_mode,
}


def main() -> None:
    display.print_logo()
    print(MENU)

    while True:
        choice = input("  Enter 1 / 2 / 3 / 4 / 5 / 6: ").strip()

        if choice == "6":
            print(f"\n  {display.Colors.DIM}Goodbye.{display.Colors.RESET}\n")
            break

        action = MODES.get(choice)
        if action:
            while True:
                action()
                key = display.get_keypress()
                if key == "up":
                    break
        else:
            display.print_error("Invalid choice — enter a number from 1 to 6.")

        display.clear()
        print(MENU)


if __name__ == "__main__":
    main()
