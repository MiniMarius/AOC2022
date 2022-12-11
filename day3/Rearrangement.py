import string

prioritysum = 0
letterMap = {}
lowers = list(string.ascii_lowercase)
for x in lowers :
    letterMap[x]=(lowers.index(x)+1)

uppers = list(string.ascii_uppercase)
for x in uppers :
    letterMap[x]=(uppers.index(x))+27

with open("input.txt", "r") as file:
    for line in file:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        for x in firstpart:
            for y in secondpart:
                if x == y:
                    prioritysum += letterMap.get(x)
                    break
            #break out of 2 inner loops if matching letters are found
            else:
                continue
            break

                    
print(prioritysum)
prioritysum = 0
with open("input.txt", "r") as file:
    # read the file line by line
    lines = file.readlines()

    # loop through the lines in groups of 3
    for i in range(0, len(lines), 3):
        # get the current group of 3 lines
        group = lines[i:i+3]
        group = [line.strip() for line in group]
        # check if there exists a matching character in all 3 lines
        # we will use the set intersection operation to find the common characters
        # in all 3 lines
        common_chars = set(group[0]) & set(group[1]) & set(group[2])

        # if the set of common characters is not empty, then there exists a
        # matching character in all 3 lines
        if common_chars:
            # print the common characters
            common_char = common_chars.pop()
            prioritysum += letterMap.get(common_char)
print(prioritysum)