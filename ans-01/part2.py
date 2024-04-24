# Advent of Code 2023 - Day 1 - Part 2 - https://adventofcode.com/2023/day/1#part2
# Date: 24/04/2024

INPUT_FILE = "input"
VALID_DIGITS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def get_first_valid_digit_in_block(block: str) -> int:
    for valid_digit in VALID_DIGITS:
        if valid_digit in block:
            return VALID_DIGITS.index(valid_digit) + 1
    return -1


def main() -> int:
    answers = []

    with open(INPUT_FILE) as f:
        lines = f.readlines()
        for line in lines:
            first_int = ""
            second_int = ""

            block = ""
            valid_digit = -1

            for i in range(len(line)):
                c = line[i]
                valid_digit = get_first_valid_digit_in_block(block)
                if valid_digit > -1:
                    first_int = str(valid_digit)
                    break
                if c.isnumeric():
                    first_int = c
                    break
                block = block + c

            block = ""
            valid_digit = -1

            for i in range(len(line), 0, -1):
                c = line[i - 1]
                valid_digit = get_first_valid_digit_in_block(block)
                if valid_digit > -1:
                    second_int = str(valid_digit)
                    break
                elif c.isnumeric():
                    second_int = c
                    break
                block = c + block

            answers.append(int(first_int + second_int))

    return sum(answers)


if __name__ == "__main__":
    total = main()
    print(f"Total: {total}")
