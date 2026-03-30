import art

print(art.logo)

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text: str, shift_amount: int, encode_or_decode: str) -> str:
    output_text = ""
    shift_amount %= len(ALPHABET)

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in ALPHABET:
            output_text += letter
        else:
            shifted_position = (ALPHABET.index(letter) + shift_amount) % len(ALPHABET)
            output_text += ALPHABET[shifted_position]

    return output_text


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    result = caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    print(f"Here is the {direction}d result: {result}")

    answer = input("\nWould you like to go again? Type 'yes' or 'no':\n").lower()
    if answer == "no":
        should_continue = False
        print("Until next time... over and out.")
