import re

# **************************************************************************************************


def min_cubes_needed_per_game(game_data):
    min_cubes = {"red": 0, "green": 0, "blue": 0}

    for set in game_data:
        for cube in set:
            number, color = cube.split()
            min_cubes[color] = max(min_cubes[color], int(number))

    return min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]


# **************************************************************************************************


def parse_game(line):
    parts = line.split(": ")[1].split(";")
    return [part.strip().split(", ") for part in parts]


# **************************************************************************************************


def main():
    total = 0
    with open("input01.txt", "r") as file:
        for line in file:
            game_data = parse_game(line)
            total += min_cubes_needed_per_game(game_data)

    print(f"Sum of set powers: {total}")


# **************************************************************************************************

if __name__ == "__main__":
    main()
