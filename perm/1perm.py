#!/usr/bin/env python3

# import math
from itertools import permutations
import pprint

n = 5
nums = [i for i in range(1, n + 1)]

swap_pairs = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        swap_pairs.append((nums[i], nums[j]))
# print(swap_pairs)

def swap_elements(listo, a, b):
    """ Swap two elements in a list """
    swapped = listo.copy()
    ai, bi = listo.index(a), listo.index(b)
    swapped[bi],swapped[ai] = swapped[ai], swapped[bi]
    return swapped

def rotate_right(listo):
    """
    Rotate list items 1 to the right
    ex: [1, 2, 3, 4] --> [4, 1, 2, 3]
    """
    rot = [listo[-1]]
    rot.extend(listo[0:len(listo)-1])
    return tuple(rot)

def all_right_rotations(listo):
    """ Get all possible rotations of a list """
    res = []
    l = listo.copy()
    res.append(tuple(l))
    for i in range(len(listo) - 1):
        l = rotate_right(l)
        res.append(l)
    return res

# set of permutations
perms = set()

# add initial set of rotations i.e., [1, ..., n]
perms.update(all_right_rotations(nums))

# add rotations for each "swapped" version of the original sequence
for pair in swap_pairs:
    a, b = pair
    print(pair)
    nums_swap = swap_elements(nums, a, b)
    perms.add(tuple(nums_swap))
    perms.update(all_right_rotations(nums_swap))
sorted_perms = sorted(perms)
# pprint.pprint(sorted_perms)

real_perms = list(permutations(nums))

print(sorted(set(real_perms).difference(sorted_perms)))
