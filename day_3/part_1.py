def main(input_filepath):
    with open(input_filepath) as f:
        rucksacks = f.readlines()
        sum = 0
        for rucksack in rucksacks:
            shared_item = find_shared_item(list(rucksack))
            sum += find_priority(shared_item)
    return sum

def find_shared_item(rucksack):
    half = len(rucksack) // 2
    first_compartment, second_compartment = rucksack[:half], rucksack[half:]
    shared_item = set(first_compartment).intersection(set(second_compartment))
    return list(shared_item).pop()

def find_priority(item):
    offset = 96 if item.islower() else 38
    return ord(item) - offset

if __name__ == "__main__":
    print(main("day_3/input.txt"))
