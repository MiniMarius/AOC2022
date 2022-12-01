elfCalories = list()
calorieCount = 0

with open("input.txt", "r") as file:
    for line in file:
        if line.strip():
            calorieCount += int(line)
        else:
            elfCalories.append(calorieCount)
            calorieCount = 0

max_calories = max(elfCalories)
max_index = elfCalories.index(max_calories)
print("Most calories carried by the " + str(max_index) + "th elf, " + "calories carried: " + str(max_calories))