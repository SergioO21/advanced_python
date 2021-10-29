#!/usr/bin/python3
from typing import TypeVar, Generic

T = TypeVar('T')

def make_repeater_of(n: int) -> Generic[T]:
    """ This closure returns a function that
        returns the entered string repeated n times.
    """
    assert type(n) == int, "You can only enter integers"
    
    def repeater(string: str) -> str:
        assert type(string) == str, "You can only enter strings"
        return string * n
    return repeater


def make_division_by(n: int) -> Generic[T]:
    """ This closure returns a function that
        returns the division of an x number by n.
    """
    assert type(n) == int, "You can only enter integers"

    def divisor(x: int) -> int:
        assert type(x) == int, "You can only enter integers"
        assert n != 0, "You can't divide by zero"
        return round(x / n)
    return divisor


def run():
    # Using Using make_repeated_of function
    repeat_5 = make_repeater_of(5);
    print(repeat_5("I'm finishing the trilogy "))

    print("-" * 100)

    # Using make_division_by function
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == "__main__":
    run()
