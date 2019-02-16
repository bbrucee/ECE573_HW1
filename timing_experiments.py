from Q1.Q1 import brute_force_3sum, binary_search_3sum
from Q2.Q2 import UFQuickfind, UFQuickunion, UFQuickunionbalanced
from Q4.Q4 import farthest_pair
from Q5.Q5 import fastest_3sum
from glob import glob
from time import clock
from matplotlib import pyplot as plt
import os


# URGENT NOTICE TO FUTURE ME
# FOR FUTURE ASSIGNMENTS USE timeit AND FUNCTIONS SIMILAR TO THE main OF EACH .py
# USE pandas FOR TABLES AND PLOTS IT WILL MAKE LIFE EASIER
# RUN AND AVERAGE TRIALS FOR EACH ONE TOO
# END NOTICE


def three_sum_timing():
    input_size = []
    brute_force_time_elapsed = []
    binary_search_time_elapsed = []
    fastest_time_elapsed = []

    for datapath in glob(os.getcwd() + "\Q1\data\*"):
        input_size.append(int(datapath.split("\\")[-1].split("int")[0]))
        file = open(datapath)
        data_array = []
        for line in file.readlines():
            data_array.append(int(line))
        file.close()
        print(datapath)
        if not int(datapath.split("\\")[-1].split("int")[0]) == 8192 or not int(datapath.split("\\")[-1].split("int")[0]) == 4096:
            start_time = clock()
            brute_force_3sum(data_array)
            end_time = clock()
            brute_force_time_elapsed.append(end_time - start_time)
        else:
            brute_force_time_elapsed.append("DNF")
        start_time = clock()
        binary_search_3sum(data_array)
        end_time = clock()
        binary_search_time_elapsed.append(end_time - start_time)
        start_time = clock()
        fastest_3sum(data_array)
        end_time = clock()
        fastest_time_elapsed.append(end_time - start_time)

    input_size, brute_force_time_elapsed, binary_search_time_elapsed, fastest_time_elapsed = zip(*sorted(zip(input_size, brute_force_time_elapsed, binary_search_time_elapsed, fastest_time_elapsed)))
    columns = ('Brute Force 3 Sum', 'Binary Search 3 Sum', 'Fastest 3 Sum')
    rows = ["{} integers".format(x) for x in input_size]
    cell_text = []
    for time_tuple in zip(brute_force_time_elapsed, binary_search_time_elapsed, fastest_time_elapsed):
        cell_text.append(["{0:.10f} seconds".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q1 and Q5: 3 Sum Timing Graphs")
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 3), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 3), (0, 0))
    plt.plot(input_size[:-2], brute_force_time_elapsed[:-2])
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


def union_find_timing():

    input_size = []
    qf_time_elapsed = []
    qu_time_elapsed = []
    qub_time_elapsed = []

    for datapath in glob(os.getcwd() + "\Q2\data\*"):
        qf = UFQuickfind(8192)
        qu = UFQuickunion(8192)
        qub = UFQuickunionbalanced(8192)

        input_size.append(int(datapath.split("\\")[-1].split("pair")[0]))
        file = open(datapath)
        data_array = []
        for line in file.readlines():
            data_array.append(tuple(map(int, line.split())))
        file.close()
        print(datapath)

        start_time = clock()
        for (left, right) in data_array:
            if not qf.find(left, right):
                qf.union(left, right)
        end_time = clock()
        qf_time_elapsed.append(end_time-start_time)

        start_time = clock()
        for (left, right) in data_array:
            if not qu.find(left, right):
                qu.union(left, right)
        end_time = clock()
        qu_time_elapsed.append(end_time-start_time)

        start_time = clock()
        for (left, right) in data_array:
            if not qub.find(left, right):
                qub.union(left, right)
        end_time = clock()
        qub_time_elapsed.append(end_time-start_time)

    input_size, qf_time_elapsed, qu_time_elapsed, qub_time_elapsed = zip(
        *sorted(zip(input_size, qf_time_elapsed, qu_time_elapsed, qub_time_elapsed)))
    columns = ('Quick Find', 'Quick Union', 'Quick Union Balanced')
    rows = ["{} pairs".format(x) for x in input_size]
    cell_text = []
    for time_tuple in zip(qf_time_elapsed, qu_time_elapsed, qub_time_elapsed):
        cell_text.append(["{0:.10f} seconds".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q2: Union-Find Graphs")
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 3), (1, 0), colspan=4, rowspan=2)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 3), (0, 0))
    plt.plot(input_size, qf_time_elapsed)
    plt.title("Union-Find: Quick Find")
    plt.xlabel("Input Size (Number of Pairs)")
    plt.ylabel("Runtime (seconds)")
    plt.subplot2grid((2, 3), (0, 1))
    plt.plot(input_size, qu_time_elapsed)
    plt.title("Union-Find: Quick Union")
    plt.xlabel("Input Size (Number of Pairs)")
    plt.ylabel("Runtime (seconds)")
    plt.subplot2grid((2, 3), (0, 2))
    plt.plot(input_size, qub_time_elapsed)
    plt.title("Union-Find: Quick Union Balanced")
    plt.xlabel("Input Size (Number of Pairs)")
    plt.ylabel("Runtime (seconds)")

    fig.set_size_inches(w=6, h=5)
    plt.show()


def farthest_pair_timing():
    input_size = []
    fpair_time_elapsed = []
    num_trials = 100

    for datapath in glob(os.getcwd() + "\Q4\data\*"):
        fpair_trials = []
        input_size.append(int(datapath.split("\\")[-1].split("int")[0]))
        file = open(datapath)
        data_array = []
        for line in file.readlines():
            data_array.append(int(line))
        file.close()
        print(datapath)
        for _ in range(num_trials):
            start_time = clock()
            farthest_pair(data_array)
            end_time = clock()
            fpair_trials.append(end_time - start_time)
        fpair_time_elapsed.append(sum(fpair_trials)/num_trials)

    input_size, fpair_time_elapsed = zip(*sorted(zip(input_size, fpair_time_elapsed)))
    columns = ('Farthest Pair', )
    rows = ["{} integers".format(x) for x in input_size]
    cell_text = []
    for time_tuple in zip(fpair_time_elapsed):
        cell_text.append(["{} seconds".format(time_data) for time_data in time_tuple])

    fig = plt.figure(1)
    plt.suptitle("Q4: Farthest Pair Timing Graph")
    fig.subplots_adjust(left=0.2, top=0.8, wspace=1)

    ax = plt.subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
    ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='upper center')
    ax.axis("off")

    plt.subplot2grid((2, 2), (0, 0),  colspan=2, rowspan=1)
    plt.plot(input_size, fpair_time_elapsed)
    plt.title("Farthest Pair")
    plt.xlabel("Input Size (Length of Array)")
    plt.ylabel("Runtime (seconds)")

    fig.set_size_inches(w=6, h=5)
    plt.show()


def main():
    three_sum_timing()
    union_find_timing()
    farthest_pair_timing()


if __name__ == '__main__':
    main()
