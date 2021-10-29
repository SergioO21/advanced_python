#!/usr/bin/python3

def even_or_odd(number: int) -> str:
    initial: str = "- The number entered is "
    return "".join([initial, "Even"]) if number % 2 == 0 else "".join([initial, "Odd"])


def run():
    print("\n", even_or_odd(int(input("\nInsert a number to check: "))))


if __name__ == "__main__":
    run()
