from constants import ROUND_COMBINATIONS, WIN_SCORE, LOSS_SCORE, DRAW_SCORE
from shape import Shape


def find_total_score(rounds_filepath):
    with open(rounds_filepath) as f:
        rounds = f.readlines()
        total = 0
        for round in rounds:
            encrypted_opponent, result = round.strip().split(" ")
            encrypted_player = find_player_shape(encrypted_opponent, result)
            player, opponent = Shape.build(encrypted_player), Shape.build(encrypted_opponent)

            total += play(player, opponent) + player.score

    return total


def find_player_shape(encrypted_opponent, result):
    return ROUND_COMBINATIONS[encrypted_opponent][result]


def play(player, opponent):
    if player > opponent:
        return WIN_SCORE
    elif player < opponent:
        return LOSS_SCORE
    elif player == opponent:
        return DRAW_SCORE


if __name__ == "__main__":
    print(find_total_score("day_2/input.txt"))
