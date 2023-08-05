import time


if __name__ == "__main__":

    with open("input.txt", "r") as f:
        seq = f.readlines()[0].strip()

    start = time.time()
    v = seq.count("(") - seq.count(")")
    print(f"Part 1 time (ms): {(time.time() - start)*1e6}")
    print(f"Part 1 Solution: {v}")

    start = time.time()
    floor = 0
    basement_index = 0
    for i, char in enumerate(seq):
        if char == "(":
            floor += 1
        else:
            floor -= 1
        if basement_index == 0 and floor == -1:
            basement_index = i + 1
            break
    print(f"Part 2 time (ms): {(time.time() - start)*1e6}")
    print(f"Part 2 Solution: {basement_index=}")

