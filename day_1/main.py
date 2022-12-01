import heapq

calories = []
heapq.heapify(calories)

with open("day_1/input.txt") as f:
    food_items = f.readlines() + ["\n"]
    elf_total = 0
    for food in food_items:
        if food == "\n":
            heapq.heappush(calories, elf_total)
            elf_total = 0
        else:
            elf_total += int(food)

# part 1
print(heapq.nlargest(1, calories)[0])

# part 2
top_three_elves = heapq.nlargest(3, calories)
print(sum(top_three_elves))
