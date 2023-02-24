def find_max_calorie_elf(calories_list):
    # Initialize the dictionary to store the total Calories for each Elf
    calories = {}
    current_elf = "Elf 1"
    calories[current_elf] = 0

    # Initialize a counter to keep track of the current Elf
    counter = 1

    # Iterate through the list of Calories and update the total Calories for each Elf
    for calorie in calories_list:
        if calorie == "":
            counter += 1
            current_elf = "Elf " + str(counter)
            calories[current_elf] = 0
        elif calorie.isnumeric():
            calories[current_elf] += int(calorie)
        else:
            print("Invalid input: " + calorie)

    # Find the Elf with the most Calories and print the Elf's name and total Calories
    max_calories = max(calories.values())
    max_elf = [key for key in calories if calories[key] == max_calories]
    print("The Elf carrying the most Calories is " +
          max_elf[0] + " with a total of " + str(max_calories) + " Calories.")


def main():
# Read the input from the file and split the lines into a list of strings
    calories_list = open("input01.txt").read().splitlines()

    # Find the Elf carrying the most Calories
    find_max_calorie_elf(calories_list)


if __name__ == "__main__":
    main()

#solution: 70698

#The Elf carrying the most Calories is Elf 65 with a total of 70698 Calories.