from Q1.Q1 import brute_force_3sum, binary_search_3sum
from Q2.Q2 import UFQuickfind, UFQuickunion, UFQuickunionbalanced
from Q4.Q4 import farthest_pair
from Q5.Q5 import fastest_3sum
from glob import glob
from time import time


def three_sum_timing():
    start_time = time()
    brute_force_3sum([1,2,3])
    binary_search_3sum([1,2,3])
    fastest_3sum([1,2,3])
    end_time = time()
    time_elasped = end_time - start_time
    print(time_elasped)
    pass


def union_find_timing():
    start_time = time()

    A = UFQuickfind(8192)
    B = UFQuickunion(8192)
    C = UFQuickunionbalanced(8192)

    for (left, right) in [(1,2), (2,3), (3,4)]:
        if not A.find(left, right):
            A.union(left, right)
        if not B.find(left, right):
            B.union(left, right)
        if not C.find(left, right):
            C.union(left, right)

    end_time = time()
    time_elasped = end_time - start_time
    print(time_elasped)
    pass


def farthest_pair_timing():
    start_time = time()
    farthest_pair([1,2,3])
    end_time = time()
    time_elasped = end_time - start_time
    print(time_elasped)
    pass


three_sum_timing()
union_find_timing()
farthest_pair_timing()
