#!/usr/bin/env python3

def moores_voting(arr):
    candidate, count = arr[0], 0
    for a in arr:
        count += [-1, 1][a == candidate]
        if count == 0:
            candidate, count = a, 1

    return [-1, candidate][arr.count(candidate) > len(arr) // 2 ]

def main():
    filename = "./rosalind_maj.txt"
    with open(filename, "r") as f:
        n, size = f.readline().strip().split(" ")
        arrays = [tuple(map(int, a.strip().split(" "))) for a in islice(f, 0, None)]

    print(*[moores_voting(arr) for arr in arrays], end = " ")


if __name__ == "__main__":
    main()
