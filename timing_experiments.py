from Q1.Q1 import brute_force_3sum, binary_search_3sum
from Q2.Q2 import UFQuickfind, UFQuickunion, UFQuickunionbalanced
from Q4.Q4 import farthest_pair
from Q5.Q5 import fastest_3sum
from glob import glob
from time import time
from matplotlib import pyplot as plt
import os


def three_sum_timing():
    brute_force_time_elapsed = []
    binary_search_time_elapsed = []
    fastest_time_elapsed = []
    input_size = []
    
    for datapath in glob(os.getcwd() + "\Q1\data\*"):
        input_size.append(datapath.split("\\")[-1].split("int")[0])
        file = open(datapath)
        data_array = []
        for line in file.readlines():
            data_array.append(int(line))
        file.close()

        start_time = time()
        brute_force_3sum(data_array)
        end_time = time()
        brute_force_time_elapsed.append(end_time - start_time)
        start_time = time()
        binary_search_3sum(data_array)
        end_time = time()
        binary_search_time_elapsed.append(end_time - start_time)
        start_time = time()
        fastest_3sum(data_array)
        end_time = time()
        fastest_time_elapsed.append(end_time - start_time)

    columns = ('Brute Force 3 Sum', 'Binary Search 3 Sum', 'Fastest 3 Sum')
    rows = ["{} integers".format(x) for x in input_size]
    cell_text = []
    for time_tuple in zip(brute_force_time_elapsed, binary_search_time_elapsed, fastest_time_elapsed):
        cell_text.append(["{} seconds".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q1 and Q5: 3 Sum Timing Graphs")
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 3), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 3), (0, 0))
    plt.plot(input_size, brute_force_time_elapsed)
    plt.title("Brute Force 3 Sum")
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")
    plt.subplot2grid((2, 3), (0, 1))
    plt.plot(input_size, binary_search_time_elapsed)
    plt.title("Binary Search 3 Sum")
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")
    plt.subplot2grid((2, 3), (0, 2))
    plt.plot(input_size, fastest_time_elapsed)
    plt.title("Fastest 3 Sum")
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")

    fig.set_size_inches(w=6, h=5)
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
# union_find_timing()
# farthest_pair_timing()
