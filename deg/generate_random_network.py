#!/usr/bin/env python3

import random

with open("random_net.txt", "w") as f:
    starts = list(map(str, list(range(1, 100001))))
    ends = random.choices(starts, k = 100000)
    for s, e in zip(starts, ends):
        f.write(f"{s} {e}\n")
