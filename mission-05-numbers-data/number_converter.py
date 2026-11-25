"""Convert a user-supplied decimal integer into binary and hexadecimal."""


def convert_decimal(decimal_value: int) -> tuple:
    """Return clean binary and uppercase hexadecimal strings for an integer."""
    binary_str = bin(decimal_value).replace("0b", "")
    hex_str = hex(decimal_value).replace("0x", "").upper()
    return binary_str, hex_str


def main() -> None:
    """Prompt for a decimal integer and print its binary and hexadecimal forms."""
    raw_input_value = input("Enter a decimal integer: ").strip()
    try:
        decimal_value = int(raw_input_value)
    except ValueError:
        print("Invalid input: please enter a valid whole decimal number.")
        return

    binary_result, hex_result = convert_decimal(decimal_value)
    print(f"Decimal:     {decimal_value}")
    print(f"Binary:      {binary_result}")
    print(f"Hexadecimal: {hex_result}")


if __name__ == "__main__":
    main()
