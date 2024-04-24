# Advent of Code 2023 - Day 1 - Part 1 - https://adventofcode.com/2023/day/1#part2
# Date: 24/04/2024

INPUT_FILE = "input"


def main():
    answers = []

    with open(INPUT_FILE) as f:
        lines = f.readlines()
        for line in lines:
            first_int = ""
            second_int = ""

            for i in range(len(line)):
                char = line[i]
                if char.isnumeric():
                    first_int = char
                    break

            for i in range(len(line), 0, -1):
                char = line[i - 1]
                if char.isnumeric():
                    second_int = char
                    break

            answers.append(int(first_int + second_int))

    return sum(answers)


if __name__ == "__main__":
    total = main()
    print(f"Total: {total}")
