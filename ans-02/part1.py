INPUT_FILE = "input"

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def parse_line(line: str) -> tuple[int, list]:
    title, games = line.split(":")

    game_number = int(title.split(" ")[1])

    scores = games.split(";")
    parsed_scores = []

    for score in scores:
        colors = [color.strip() for color in score.split(",")]
        # print(colors)
        parsed_scores.append(
            {color.split(" ")[1]: int(color.split(" ")[0]) for color in colors}
        )

    return game_number, parsed_scores


def is_possible_game(scores: list) -> bool:
    for score in scores:
        if score.get("red", None) and score["red"] > MAX_RED:
            return False
        if score.get("green", None) and score["green"] > MAX_GREEN:
            return False
        if score.get("blue", None) and score["blue"] > MAX_BLUE:
            return False
    return True


def main() -> int:
    total = 0

    with open(INPUT_FILE) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            game_number, scores = parse_line(line)

            if is_possible_game(scores):
                total += game_number

    return total


if __name__ == "__main__":
    total = main()
    print(f"Total: {total}")
