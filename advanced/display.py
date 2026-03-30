import os
import sys
import time

from config import TYPEWRITER_SPEED, BRUTE_FORCE_DELAY

LOGO = """
  ____                               ____ _       _
 / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __
| |   / _` |/ _ \\/ __|/ _` | '__| | |   | | '_ \\| '_ \\ / _ \\ '__|
| |__| (_| |  __/\\__ \\ (_| | |    | |___| | |_) | | | |  __/ |
 \\____\\__,_|\\___||___/\\__,_|_|     \\____|_| .__/|_| |_|\\___|_|
                                           |_|
         Advanced Edition — encode · decode · crack · analyze
"""


class Colors:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    GREEN   = "\033[92m"
    RED     = "\033[91m"
    CYAN    = "\033[96m"
    MAGENTA = "\033[95m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"


def clear() -> None:
    os.system("clear" if os.name == "posix" else "cls")


def typewriter(text: str, speed: float = TYPEWRITER_SPEED) -> None:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def print_logo() -> None:
    typewriter(Colors.CYAN + LOGO + Colors.RESET, speed=0.004)


def print_result(mode: str, original: str, result: str) -> None:
    color = Colors.GREEN if mode == "encode" else Colors.MAGENTA
    print(f"\n  {Colors.DIM}original :{Colors.RESET} {original}")
    print(f"  {color}{mode}d  :{Colors.RESET} {Colors.BOLD}{result}{Colors.RESET}\n")


def print_brute_force(results: list[tuple[int, str]]) -> None:
    print(f"\n  {Colors.CYAN}{Colors.BOLD}Brute Force — All 26 Shifts{Colors.RESET}\n")
    print(f"  {'Shift':<8} {'Decrypted'}")
    print(f"  {'─' * 6}   {'─' * 50}")
    for shift, text in results:
        time.sleep(BRUTE_FORCE_DELAY)
        print(f"  {Colors.YELLOW}{shift:<8}{Colors.RESET} {text}")
    print()


def print_frequency_result(shift: int, result: str, original: str) -> None:
    print(f"\n  {Colors.CYAN}{Colors.BOLD}Frequency Analysis Result{Colors.RESET}")
    print(f"\n  {Colors.DIM}Most likely shift:{Colors.RESET} {Colors.YELLOW}{shift}{Colors.RESET}")
    print(f"  {Colors.DIM}original         :{Colors.RESET} {original}")
    print(f"  {Colors.GREEN}decrypted        :{Colors.RESET} {Colors.BOLD}{result}{Colors.RESET}\n")


def print_file_result(mode: str, output_path: str) -> None:
    color = Colors.GREEN if mode == "encode" else Colors.MAGENTA
    print(f"\n  {color}{Colors.BOLD}File {mode}d successfully.{Colors.RESET}")
    print(f"  Saved to: {Colors.CYAN}{output_path}{Colors.RESET}\n")


def print_error(message: str) -> None:
    print(f"\n  {Colors.RED}Error: {message}{Colors.RESET}\n")


def divider() -> None:
    print(f"  {Colors.DIM}{'─' * 58}{Colors.RESET}")
