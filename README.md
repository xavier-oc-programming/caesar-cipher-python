# Caesar Cipher

A command-line Caesar cipher tool written in Python — built twice, at different points in my learning journey, to show how my skills grew.

The **original** was written in 2024 on Day 8 of learning Python. The **advanced rebuild** came later, rewriting the same concept from scratch using everything I'd picked up since: OOP, type hints, dataclasses, frequency analysis cryptanalysis, Vigenère cipher support, file I/O, ANSI color output, and a clean multi-module architecture.

Both versions are playable through a shared launcher menu.

> Built as Day 8 of [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

## Getting Started

**Prerequisites:** Python 3.10+ — no external dependencies.

```bash
# Clone the repo
git clone https://github.com/xavier-oc-programming/caesar-cipher-python.git
cd caesar-cipher-python

# Launch the menu
python menu.py
```

Or run either version directly:

```bash
python original/main.py
python advanced/main.py
```

---

## The Menu

```
  ____                               ____ _       _
 / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __
| |   / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |    | |___| | |_) | | | |  __/ |
 \____\__,_|\___||___/\__,_|_|     \____|_| .__/|_| |_|\___|_|
                                           |_|

  Select a version:

  1  Original   — Day 8 of 100 Days of Code · beginner · plain text
  2  Advanced   — rebuild · OOP · Vigenère · cryptanalysis · file I/O
  3  Quit

  Enter 1 / 2 / 3:
```

---

## Original Version (`original/`)

Built during the course using only the Python basics covered up to Day 8: loops, functions, conditionals, string manipulation, and imports.

**Demo**

```
  encode or decode? encode
  Type your message: meet me at midnight
  Type the shift number: 5

  original : meet me at midnight
  encoded  : rjjy rj fy rnionlmy
```

**Features**

- Encode and decode messages with a numeric shift
- Non-alphabetic characters (numbers, spaces, punctuation) passed through unchanged
- Modulo wrap-around — shift values larger than 26 are handled correctly
- Restart loop — run multiple times without relaunching

**Structure** — 2 files, procedural

| File | Purpose |
|---|---|
| `main.py` | All game logic and the run loop |
| `art.py` | ASCII art logo |

---

## Advanced Rebuild (`advanced/`)

Came back to the same concept after building up significantly more Python experience. Same core idea, completely rewritten to demonstrate the patterns and techniques I'd learned.

### Features

**Caesar Cipher**
Each letter is shifted a fixed number of positions along the alphabet. Shift 3 turns A→D, B→E, Z→C. Non-letters (spaces, numbers, punctuation) pass through unchanged. The terminal clears before each mode so only the current interaction is on screen.

**Vigenère Cipher**
A stronger cipher — instead of one fixed shift, a keyword sets a different shift for each letter. The keyword repeats across the message, so `KEY` shifts letters by 10, 4, 24 in rotation. Far harder to crack than a single-shift Caesar.

**Brute Force**
Since Caesar only has 26 possible shifts, the tool tries all of them and prints every result, animated line by line. Scan the list for the one that reads as real English.

**Frequency Analysis**
In English, some letters appear far more often than others — `e` is most common, followed by `t`, `a`, `o`, `i`, `n`. This tool counts letter frequencies in the ciphertext, then compares the distribution against expected English frequencies across all 26 shifts using sum of squared errors. The closest-matching shift is returned as the most likely answer. Works best on longer messages; short texts may not carry enough signal.

**File Encrypt / Decrypt**
Encrypts or decrypts an entire `.txt` file using a Caesar shift.

How to use:
1. Save your message as a plain `.txt` file anywhere on your computer.
2. Run the tool and enter the full file path (e.g. `/Users/you/message.txt`).
3. Enter a path for the output file (e.g. `/Users/you/encrypted.txt`).
4. Choose a shift — use the same shift and the opposite direction to reverse it.
5. The output file is created automatically if it doesn't exist.

**UX details**
- Terminal clears between every interaction so only the current output is shown
- Each mode opens with a brief plain-English explanation of how it works before prompting for input
- ANSI color output — green for encoded, magenta for decoded, cyan for headers, yellow for shift values
- Typewriter intro — logo animates character by character on launch

### Structure — 6 modules, OOP

| File | Purpose |
|---|---|
| `main.py` | Entry point, menu loop, mode dispatch, in-app cipher explanations |
| `cipher.py` | `CaesarCipher` and `VigenereCipher` dataclasses with `CipherMode` enum |
| `cracker.py` | `CipherCracker` class — brute force and frequency analysis |
| `display.py` | `Colors`, `clear()`, typewriter, formatted result output, brute force table |
| `file_io.py` | `FileHandler` class — `.txt` file encrypt/decrypt via `pathlib` |
| `config.py` | `ALPHABET`, `ENGLISH_FREQ` dict, animation timing constants |

---

## Project Structure

```
caesar-cipher-python/
├── menu.py                 # Top-level launcher
├── README.md
├── .gitignore
├── .python-version
├── requirements.txt
├── docs/
│   └── COURSE_NOTES.md     # Original course exercise prompts and lesson breakdown
├── original/               # Day 8 beginner version (2024)
│   ├── main.py
│   └── art.py
└── advanced/               # Rebuilt version (2025)
    ├── main.py
    ├── cipher.py
    ├── cracker.py
    ├── display.py
    ├── file_io.py
    └── config.py
```

---

## What I Learned (Original, 2024)

- Defining functions with parameters and calling them with arguments
- Positional vs keyword arguments
- Using `list.index()` to find a character's position in the alphabet
- Modulo arithmetic for alphabet wrap-around (`shifted %= 26`)
- Importing names from a separate module
- Using a `while` loop to build a restart mechanism

## What I Applied (Advanced Rebuild, 2025)

- OOP — encapsulating cipher logic in `CaesarCipher` and `VigenereCipher` dataclasses
- `Enum` for strongly-typed `CipherMode` (encode/decode) instead of raw strings
- Full type hints throughout (`str`, `int`, `list[tuple[int, str]]`, `float`)
- Separation of concerns — logic, display, I/O, and config in isolated modules
- Frequency analysis — scoring candidate decryptions against English letter frequency distributions using sum of squared errors
- ANSI escape codes for terminal color output
- `sys.stdout.write` + `sys.stdout.flush()` for character-by-character typewriter animation
- `pathlib.Path` for clean, cross-platform file reading and writing
- Input validation and error handling at system boundaries
- `os.system("clear")` for terminal clearing between interactions

---

## Part of My 100 Days of Code Journey

This is **Day 8** of my Python learning journey. The original was written at the very start; the rebuild shows where I am now.

> Original: 2024 · Rebuild: 2025
