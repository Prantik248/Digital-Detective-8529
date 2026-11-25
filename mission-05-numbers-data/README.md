# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 was to convert numbers manually between decimal, binary, and hexadecimal, verify every calculation inside the Python interactive shell, build and test `number_converter.py`, and explain how computers store characters using ASCII and UTF-8 encoding.

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
|---|---|
| Convert decimal `13` to binary. | Divide repeatedly by 2 and read remainders bottom-to-top:<br>`13 ÷ 2 = 6` R `1`<br>`6 ÷ 2 = 3` R `0`<br>`3 ÷ 2 = 1` R `1`<br>`1 ÷ 2 = 0` R `1`<br>**Answer:** `1101` |
| Convert decimal `25` to binary. | Divide repeatedly by 2 and read remainders bottom-to-top:<br>`25 ÷ 2 = 12` R `1`<br>`12 ÷ 2 = 6` R `0`<br>`6 ÷ 2 = 3` R `0`<br>`3 ÷ 2 = 1` R `1`<br>`1 ÷ 2 = 0` R `1`<br>**Answer:** `11001` |
| Convert binary `1010` to decimal. | Multiply each bit by its power of 2:<br>`(1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)` = `8 + 0 + 2 + 0`<br>**Answer:** `10` |
| Convert binary `1101` to decimal. | Multiply each bit by its power of 2:<br>`(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)` = `8 + 4 + 0 + 1`<br>**Answer:** `13` |
| Convert hexadecimal `A` to decimal. | In base 16, `A = 10`:<br>`10 × 16⁰ = 10 × 1`<br>**Answer:** `10` |
| Convert hexadecimal `1F` to decimal. | Multiply each digit by powers of 16 (`F = 15`):<br>`(1 × 16¹) + (15 × 16⁰)` = `16 + 15`<br>**Answer:** `31` |
| Convert binary `1111` to hexadecimal. | Binary `1111` in decimal is `8 + 4 + 2 + 1 = 15`. In base 16, `15` is `F`.<br>**Answer:** `F` |

---

### Task 5.2 — Verify using Python
Verified inside the `python3` interactive REPL:

| Check | Python expression tested | Result | Matches manual calculation? |
|---|---|---|---|
| Decimal 13 -> Binary | `bin(13)` | `'0b1101'` | Yes (`1101`) |
| Decimal 25 -> Binary | `bin(25)` | `'0b11001'` | Yes (`11001`) |
| Binary 1010 -> Decimal | `int('1010', 2)` | `10` | Yes (`10`) |
| Binary 1101 -> Decimal | `int('1101', 2)` | `13` | Yes (`13`) |
| Decimal 10 -> Hexadecimal | `hex(10)` | `'0xa'` | Yes (`A`) |
| Hexadecimal A -> Decimal | `int('A', 16)` | `10` | Yes (`10`) |
| Decimal 31 -> Hexadecimal | `hex(31)` | `'0x1f'` | Yes (`1F`) |
| Hexadecimal 1F -> Decimal | `int('1F', 16)` | `31` | Yes (`31`) |
| Binary 1111 -> Hexadecimal | `hex(int('1111', 2))` | `'0xf'` | Yes (`F`) |

---

### Task 5.3 — Build a small number converter
Created `mission-05-numbers-data/number_converter.py` and ran it from Terminal with four positive test numbers:

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| `13` | `1101` | `D` |
| `25` | `11001` | `19` |
| `42` | `101010` | `2A` |
| `255` | `11111111` | `FF` |

**How `bin()` and `hex()` work:**  
Python's `input()` reads text as a string, so `int()` first converts that text into an integer object. Then `bin(n)` takes the integer `n` and returns its base-2 representation prefixed with `'0b'`, while `hex(n)` takes `n` and returns its base-16 representation prefixed with `'0x'`. Removing those prefixes (and calling `.upper()` on hex letters) formats the output cleanly for the user.

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes:**
  - Uppercase `'A'` = **`65`** (verified with `ord('A')`)
  - Lowercase `'a'` = **`97`** (verified with `ord('a')`)
- **Why an encoding standard is needed:** Computers can only store numbers (bits of `0` and `1`) in memory and on disk, so an encoding standard acts as a shared lookup table that maps every letter, digit, and symbol to a consistent numeric code across all devices.
- **Character outside basic ASCII:** The Indian Rupee symbol **`₹`** (Unicode `U+20B9`, UTF-8 bytes `b'\xe2\x82\xb9'`) or accented **`é`** (`U+00E9`) cannot be represented in 7-bit basic ASCII (`0–127`), so UTF-8 encodes it using multiple bytes.

## 3. Commands / tools used
- `python3` — Launched the interactive Python REPL to test `bin()`, `hex()`, `int(..., base)`, `ord()`, and `.encode('utf-8')`.
- `python3 number_converter.py` — Ran the number-converter program from Terminal with test inputs (`13`, `25`, `42`, `255`).
- `input()`, `int()`, `bin()`, `hex()` — Built-in Python functions used inside `number_converter.py`.

## 4. My understanding
All numbers and text inside a computer ultimately reduce to binary digits (`0` and `1`). Binary matches hardware on/off voltage states, hexadecimal acts as a compact shorthand for groups of four bits, and encoding standards like ASCII and UTF-8 let computers translate numbers back into readable human text reliably.

## 5. Difficulties faced
Remembering that Python's `bin()` and `hex()` return strings starting with `'0b'` and `'0x'` (rather than bare digits) and handling non-numeric input gracefully required careful testing.

## 6. How I resolved them
I stripped the `'0b'` and `'0x'` prefixes in `convert_decimal()` and wrapped `int(raw_input_value)` inside a `try ... except ValueError` block so invalid entries print a clear message instead of crashing.

## 7. Evidence / files
- [number_converter.py](number_converter.py)
- `mission-05-numbers-data/README.md`
- [Python REPL verification screenshot](../evidence/mission-05/01-python-repl-verification.png)
- [Number converter test runs screenshot](../evidence/mission-05/02-number-converter-runs.png)

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Status:** Committed locally on `main` (ready to push to GitHub).
