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

    # Sort the Elves by total Calories in descending order
    sorted_calories = sorted(
        calories.items(), key=lambda x: x[1], reverse=True)

    # Return the top three Elves
    return sorted_calories[:3]


def main():
    # Read the input from the file and split the lines into a list of strings
    calories_list = open("input01.txt").read().splitlines()

    # Find the top three Elves carrying the most Calories
    top_elves = find_max_calorie_elf(calories_list)

    # Calculate the total Calories carried by the top three Elves
    total_calories = sum(elf[1] for elf in top_elves)
    print("The top three Elves are carrying a total of " +
          str(total_calories) + " Calories.")


if __name__ == "__main__":
    main()

# solution: 206643

# The top three Elves are carrying a total of 206643 Calories.
