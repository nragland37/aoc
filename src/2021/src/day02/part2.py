def main():
    data = open("input01.txt").read().splitlines()
    data = [x.split() for x in data]
    commands = [(x[0], int(x[1])) for x in data]

    aim, h, d = 0, 0, 0

    for cmd, val in commands:
        if cmd == "forward":
            h += val
            d += val * aim
        elif cmd == "down":
            aim += val
        elif cmd == "up":
            aim -= val
        else:
            raise ValueError("invalid")

    print(h * d)


if __name__ == "__main__":
    main()
