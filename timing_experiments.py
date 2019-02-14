from Q1.Q1 import brute_force_3sum, binary_search_3sum
from Q2.Q2 import UFQuickfind, UFQuickunion, UFQuickunionbalanced
from Q4.Q4 import farthest_pair
from Q5.Q5 import fastest_3sum
from glob import glob
from time import time
from matplotlib import pyplot as plt


def three_sum_timing():
    start_time = time()
    brute_force_3sum([1,2,3])
    binary_search_3sum([1,2,3])
    fastest_3sum([1,2,3])
    end_time = time()
    time_elapsed = end_time - start_time
    print(time_elapsed)

    brute_force_time_elapsed = [10, 20, 30, 40, 50, 60, 70, 80]
    binary_search_time_elapsed = [1, 2, 3, 4, 5, 6, 7, 8]
    fastest_time_elapsed = [1, 2, 3, 4, 5, 6, 7, 8]

    file_sizes = [8, 32, 128, 512, 1024, 4096, 4192, 8192]
    plt.plot(file_sizes, brute_force_time_elapsed)
    plt.plot(file_sizes, binary_search_time_elapsed)
    plt.plot(file_sizes, fastest_time_elapsed)
    # plt.legend()
    # plt.title()
    plt.show()
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
    time_elapsed = end_time - start_time
    print(time_elapsed)

    qf_time_elapsed = [10, 20, 30, 40, 50, 60, 70]
    qu_time_elapsed = [1, 2, 3, 4, 5, 6, 7]
    qub_time_elapsed = [1, 2, 3, 4, 5, 6, 7]

    file_sizes = [8, 32, 128, 512, 1024, 4096, 8192]
    plt.plot(file_sizes, qf_time_elapsed)
    plt.plot(file_sizes, qu_time_elapsed)
    plt.plot(file_sizes, qub_time_elapsed)
    # plt.legend()
    # plt.title()
    plt.show()
    pass


def farthest_pair_timing():
    start_time = time()
    farthest_pair([1,2,3])
    end_time = time()
    time_elapsed = end_time - start_time
    print(time_elapsed)

    fpair_time_elapsed = [1, 2, 3, 4, 5, 6, 7, 8]
    file_sizes = [8, 32, 128, 512, 1024, 4096, 4192, 8192]

    plt.plot(file_sizes, fpair_time_elapsed)
    # plt.legend()
    # plt.title()
    plt.show()
    pass


three_sum_timing()
union_find_timing()
farthest_pair_timing()
