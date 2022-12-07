def main():
    aim = horiz = depth = 0
    for line in open('input01.txt'):
        cmd, x = line.split()
        x = int(x)

        if cmd == 'down':
            depth += x
        elif cmd == 'up':
            depth -= x
        else:
            horiz += x

    answer = horiz * depth
    print(answer)


if __name__ == '__main__':
    main()

#solution: 1882980
