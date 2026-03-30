import subprocess
import sys
from pathlib import Path

LOGO = """
  ____                               ____ _       _
 / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __
| |   / _` |/ _ \\/ __|/ _` | '__| | |   | | '_ \\| '_ \\ / _ \\ '__|
| |__| (_| |  __/\\__ \\ (_| | |    | |___| | |_) | | | |  __/ |
 \\____\\__,_|\\___||___/\\__,_|_|     \\____|_| .__/|_| |_|\\___|_|
                                           |_|
"""

MENU = """
  Select a version:

  1  Original   — Day 8 of 100 Days of Code · beginner · plain text
  2  Advanced   — rebuild · OOP · Vigenère · cryptanalysis · file I/O
  3  Quit

  Enter 1 / 2 / 3: """

BASE = Path(__file__).parent


def launch(script: Path) -> None:
    subprocess.run([sys.executable, str(script)])


def main() -> None:
    print(LOGO)

    while True:
        choice = input(MENU).strip()

        if choice == "1":
            launch(BASE / "original" / "main.py")
        elif choice == "2":
            launch(BASE / "advanced" / "main.py")
        elif choice == "3":
            print("\n  Goodbye.\n")
            break
        else:
            print("\n  Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
