# Day 8 — Course Notes

> Original exercise prompts from [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.

---

## Lesson Topics

1. **Functions with Inputs** — Parameters vs arguments. Passing single and multiple inputs to functions.
2. **Positional vs Keyword Arguments** — Positional (order matters) vs keyword (named, order-independent) arguments.
3. **Caesar Cipher 1** — Build an `encrypt()` function. Shift letters forward using `index()` and modulo wrap-around.
4. **Caesar Cipher 2** — Add `decrypt()`, then combine both into a single `caesar()` function using a `direction` parameter.
5. **Caesar Cipher 3** — Complete program: import ASCII logo, handle non-alphabetic characters, add a restart loop.

---

## Exercise Prompts

### Caesar Cipher 1
- Create `encrypt(original_text, shift_amount)` — shift each letter forward in the alphabet.
- Handle wrap-around past `z` using modulo (`%`).
- Call the function with user input for text and shift.

### Caesar Cipher 2
- Create `decrypt(original_text, shift_amount)` — shift each letter backward.
- Combine `encrypt` and `decrypt` into a single `caesar(original_text, shift_amount, encode_or_decode)` function.
- Hint: multiply shift by `-1` for decoding.

### Caesar Cipher 3
- Import and print the ASCII logo from `art.py` at startup.
- Handle numbers, symbols, and spaces — pass them through unchanged.
- Add a `while` loop so the user can run the program multiple times without restarting.

---

## Key Concepts Introduced

| Concept | Example |
|---|---|
| Function parameter | `def greet(name):` |
| Function argument | `greet("Angela")` |
| Positional argument | `greet_with("Angela", "London")` |
| Keyword argument | `greet_with(location="London", name="Angela")` |
| Modulo wrap-around | `shifted_position %= len(alphabet)` |
| Importing a module | `import art` / `print(art.logo)` |
