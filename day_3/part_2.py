def main(input_filepath):
    with open(input_filepath) as f:
        rucksacks = list(f.readlines())
        sum = 0
        for i in range(0, len(rucksacks), 3):
            r1, r2, r3 = rucksacks[i:i+3]
            shared_item = find_shared_item(r1, r2, r3)
            sum += find_priority(shared_item)
    return sum

def find_shared_item(r1, r2, r3):
    shared_item = set(r1).intersection(set(r2)).intersection(set(r3))
    return list(shared_item).pop()

def find_priority(item):
    offset = 96 if item.islower() else 38
    return ord(item) - offset

if __name__ == "__main__":
    print(main("day_3/input.txt"))
