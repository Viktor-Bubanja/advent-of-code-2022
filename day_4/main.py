def main(input_filepath):
    total = 0
    with open(input_filepath) as f:
        pairs = f.readlines()
        for pair in pairs:
            first_elf, second_elf = parse_assignment_pair(pair)
            first_assignment, second_assignment = parse_assignment(first_elf), parse_assignment(second_elf)
            if assignments_overlap(first_assignment, second_assignment):
                total += 1

    return total

def parse_assignment_pair(pair):
    return pair.strip().split(",")


def parse_assignment(elf):
    return tuple(int(i) for i in elf.split("-"))


# Part 1
def assignments_completely_overlap(first_assignment, second_assignment):
    return (
        first_assignment[0] >= second_assignment[0] and first_assignment[1] <= second_assignment[1]
    ) or (
        second_assignment[0] >= first_assignment[0] and second_assignment[1] <= first_assignment[1] 
    )

# Part 2
def assignments_overlap(first_assignment, second_assignment):
    return (
        first_assignment[0] >= second_assignment[0] and first_assignment[0] <= second_assignment[1]
    ) or (
        second_assignment[0] >= first_assignment[0] and second_assignment[0] <= first_assignment[1] 
    )


if __name__ == "__main__":
    print(main("day_4/input.txt"))
