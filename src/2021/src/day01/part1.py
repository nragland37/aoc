INPUT = """\
199
200
208
210
200
207
240
269
260
263
"""


def main():
    numbers = open("input01.txt").read().splitlines()
    # numbers = [int(line.strip()) for line in INPUT.splitlines()]  # example input
    print(numbers[0], "(N/A - no previous measurement)")

    count = 0

    for index in range(1, len(numbers)):
        currentNum = numbers[index]
        prevNum = numbers[index - 1]

        if currentNum > prevNum:
            print(currentNum, "(increased)")
            count += 1
        else:
            print(currentNum, "(decreased)")

    print("")
    print(count)


if __name__ == "__main__":
    main()
