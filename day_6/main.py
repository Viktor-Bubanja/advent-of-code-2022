from input import *

def main(datastream):
    assert len(datastream) >= 4

    for i in range(13, len(datastream)):
        last_14_chars = datastream[i-13:i+1]
        if len(set(last_14_chars)) == 14:
            return i + 1


if __name__ == "__main__":
    print(main(input))
