data = open("input01.txt", "r", encoding="utf-8").read().splitlines()
depths = [int(x) for x in data]

# We don't need to sum the elements, because comparing:
#  depths[i] + depths[i+1] + depths[i+2] < depths[i+1] + depths[i+2] + depths[i+3]
# has the same resuts as comparing:
#  depths[i] < depths[i+3]

increases = sum(x < y for x, y in zip(depths, depths[3:]))
print("Solution:", increases)

#Solution: 1252