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

    max_calories = max(calories.values())
    max_elf = [key for key in calories if calories[key] == max_calories]
    print(f"{max_calories}\n{max_elf}")


def main():
    calories_list = open("input01.txt").read().splitlines()
    find_max_calorie_elf(calories_list)


if __name__ == "__main__":
    main()
