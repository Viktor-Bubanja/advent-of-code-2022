def main(input_filepath):
    with open(input_filepath) as f:
        lines = (line for line in f.readlines())
        crates = get_crates(lines)
        moves = get_moves(lines)
    crates = move_crates(crates, moves)

    return find_top_crates(crates)

def get_crates(lines):
    crates = {}
    for line in lines:
        for count, index in enumerate(range(1, len(line) - 1, 4)):
            stack_number = count + 1
            crate = line[index]
            if crate.isnumeric():
                return crates
            if not crate.isspace():
                crate_stack = [crate] + crates.get(stack_number, [])
                crates[stack_number] = crate_stack

    return crates

def get_moves(lines):
    moves = []
    next(lines) # get rid of blank line
    for line in lines:
        words = line.strip().split(" ")
        moves.append(tuple(int(w) for w in words[1:6:2]))

    return moves

# Part 1
def move_crates(crates, moves):
    crates = dict(crates)
    for move in moves:
        number_crates, from_, to = move
        for _ in range(number_crates):
            crates[to] = crates[to] + [crates[from_].pop()]
    return crates

# Part 2
def move_crates2(crates, moves):
    crates = dict(crates)
    for move in moves:
        number_crates, from_, to = move
        crates_to_add = []
        for _ in range(number_crates):
            crates_to_add.append(crates[from_].pop())
        crates[to] = crates[to] + list(reversed(crates_to_add))
    return crates

def find_top_crates(crates):
    output = []
    for i in range(1, len(crates) + 1):
        if crates[i]:
            output.append(crates[i][-1])
    return ''.join(output)


if __name__ == "__main__":
    print(main("day_5/test_input.txt"))
