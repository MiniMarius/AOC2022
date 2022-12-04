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
