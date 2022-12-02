totalscorePart1 = 0
with open("input.txt", "r") as file:
    for line in file:
        if "A X" in line:
            totalscorePart1 += 4
        if "A Y" in line:
            totalscorePart1 += 8
        if "A Z" in line:
            totalscorePart1 += 3
        if "B X" in line:
            totalscorePart1 += 1
        if "B Y" in line:
            totalscorePart1 += 5
        if "B Z" in line:
            totalscorePart1 += 9
        if "C X" in line:
            totalscorePart1 += 7
        if "C Y" in line:
            totalscorePart1 += 2
        if "C Z" in line:
            totalscorePart1 += 6
        
print("part 1: " + str(totalscorePart1))
totalscorePart2 = 0
with open("input.txt", "r") as file:
    for line in file:
        if "A X" in line:
            totalscorePart2 += 3
        if "A Y" in line:
            totalscorePart2 += 4
        if "A Z" in line:
            totalscorePart2 += 8
        if "B X" in line:
            totalscorePart2 += 1
        if "B Y" in line:
            totalscorePart2 += 5
        if "B Z" in line:
            totalscorePart2 += 9
        if "C X" in line:
            totalscorePart2 += 2
        if "C Y" in line:
            totalscorePart2 += 6
        if "C Z" in line:
            totalscorePart2 += 7
        
print("part 2: " + str(totalscorePart2))


