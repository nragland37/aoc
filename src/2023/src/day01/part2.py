def replace_spelled_numbers(line):
    number_words = [
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
    for index, word in enumerate(number_words, start=1):
        line = line.replace(word, str(index))
    return line


# #**************************************************************************************************


def calc(lines):
    total = 0
    for line in lines:
        line = replace_spelled_numbers(line)
        digits = [ch for ch in line if ch.isdigit()]
        if digits:
            num = int(digits[0] + digits[-1])
            total += num
    return total


# **************************************************************************************************


def main():
    with open("input01.txt", "r") as file:
        lines = file.read().splitlines()
    print(calc(lines))


# **************************************************************************************************

if __name__ == "__main__":
    main()
