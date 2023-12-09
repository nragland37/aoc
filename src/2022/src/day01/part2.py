def find_max_calorie_elf(calories_list):
    calories = {}
    current_elf = "Elf 1"
    calories[current_elf] = 0
    counter = 1

    for calorie in calories_list:
        if calorie == "":
            counter += 1
            current_elf = "Elf " + str(counter)
            calories[current_elf] = 0
        elif calorie.isnumeric():
            calories[current_elf] += int(calorie)
        else:
            print("Invalid input: " + calorie)

    sorted_calories = sorted(calories.items(), key=lambda x: x[1], reverse=True)

    return sorted_calories[:3]


# **************************************************************************************************


def main():
    calories_list = open("input01.txt").read().splitlines()

    top_elves = find_max_calorie_elf(calories_list)

    total_calories = sum(elf[1] for elf in top_elves)
    print(total_calories)


# **************************************************************************************************


if __name__ == "__main__":
    main()
