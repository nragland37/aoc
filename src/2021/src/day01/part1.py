# numbers = [
#     199,
#     200,
#     208,
#     210,
#     200,
#     207,
#     240,
#     269,
#     260,
#     263,
# ]

file = open("input01.txt")
lines = file.readlines()
numbers = []

for line in lines:
    number = int(line.strip())
    numbers.append(number)

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
print("Solution:", count)

#Solution: 1226