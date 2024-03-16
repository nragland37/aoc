def calc(lines):
    total = 0

    for line in lines:
        digits = [ch for ch in line if ch.isdigit()]

        if digits:
            num = int(digits[0] + digits[-1])
            total += num

    return total


def main():
    with open("input01.txt", "r") as file:
        lines = file.read().splitlines()

    print(calc(lines))


if __name__ == "__main__":
    main()
