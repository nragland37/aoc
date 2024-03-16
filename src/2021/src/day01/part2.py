def main():
    data = open("input01.txt").read().splitlines()
    depths = [int(x) for x in data]
    increases = sum(x < y for x, y in zip(depths, depths[3:]))
    print(increases)


if __name__ == "__main__":
    main()
