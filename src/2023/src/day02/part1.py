def is_game_possible(game, max_cubes):
    for set in game:
        cube_counts = {"red": 0, "green": 0, "blue": 0}
        for cube in set:
            number, color = cube.split()
            cube_counts[color] += int(number)
            if cube_counts[color] > max_cubes[color]:
                return False
    return True


def parse_game(line):
    parts = line.split(": ")[1].split(";")
    return [part.strip().split(", ") for part in parts]


def main():
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    possible_game_ids = []

    with open("input01.txt", "r") as file:
        for line in file:
            game_id, game_data = int(line.split(":")[0].split(" ")[1]), parse_game(line)
            if is_game_possible(game_data, max_cubes):
                possible_game_ids.append(game_id)

    print(sum(possible_game_ids))


if __name__ == "__main__":
    main()
