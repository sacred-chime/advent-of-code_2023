INPUT_FILE = "input_test"


def parse_line(line):
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


def get_fewest_cubes(scores):
    fewest_cubes = {"red": 0, "green": 0, "blue": 0}

    for score in scores:
        if score.get("red", None) and score["red"] > fewest_cubes["red"]:
            fewest_cubes["red"] = score["red"]

        if score.get("green", None) and score["green"] > fewest_cubes["green"]:
            fewest_cubes["green"] = score["green"]

        if score.get("blue", None) and score["blue"] > fewest_cubes["blue"]:
            fewest_cubes["blue"] = score["blue"]

    return fewest_cubes


def main():
    total = 0

    with open(INPUT_FILE) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            game_number, scores = parse_line(line)

            fewest_cubes = get_fewest_cubes(scores)

            total += fewest_cubes["red"] * fewest_cubes["green"] * fewest_cubes["blue"]

    return total


if __name__ == "__main__":
    total = main()
    print(f"Total: {total}")
