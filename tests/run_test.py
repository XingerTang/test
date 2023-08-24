# import pytest
import time
import os
import numpy as np
import platform
import sys

def something(duration=0.000001):
    """
    Function that needs some serious benchmarking.
    """
    time.sleep(duration)
    # You may return anything you want, like the result of a computation
    return 123

# def test_my_stuff(benchmark):
#     # benchmark something
#     benchmark.extra_info['foo'] = 'bar'
#     result = benchmark(something)
#     # Extra code, to verify that the run completed correctly.
#     # Sometimes you may want to check the result, fast functions
#     # are no good if they return incorrect results :-)
#     assert result == 123

# def test_my_stuff_different_arg(benchmark):
#     # benchmark something, but add some arguments
#     result = benchmark(something, 0.001)
#     print("1234")
#     assert result == 123


def read_file(file_path):
    """
    INPUT:
    file_path: str, the path of the file to be read
    OUTPUT:
    values: 2d list of str, store the values of the records
    """
    with open(file_path, "r") as file:
        values = [line.strip().split() for line in file]

    return np.array(values)


def write_file(file_path, list_of_data):
    """
    INPUT:
    file_path: str, the path of the file to write
    list_of_data: list of str, the data to be written
    OUTPUT:
    values: 2d list of str, store the values of the records
    """
    linesep = os.linesep
    with open(file_path, "w") as file:
        for row in list_of_data:
            file.write(" ".join(row) + "\n")

def test_file():  
    # system = platform.system()
    # subset = np.floor(np.linspace(1, 1000, num=200))
    # subset = np.concatenate(([0], subset), dtype=int, casting="unsafe")

    # file_r = os.path.join("tests", "peeling.seg")
    # seg = read_file(file_r)
    # file_w = os.path.join("tests", "seg.subset.txt")
    # write_file(file_w, seg[:, subset])

    # with open(file_w) as f:
    #     i = 0
    #     for line in f:
    #         parts = line.split()
    #         i += 1
    #         print(i)
    #         parts[0]
    assess_peeling_per_generation("peeling.multi.estmaf.dosages")


def assess_peeling_per_generation(file_prefix):
    """
    assess the performance of the peeling
    """

    output_path = "tests/peeling.single.dosages"
    true_path = "tests/trueGenotypes.txt"

    new_file = np.loadtxt(output_path)
    trueGenotypes = np.loadtxt(true_path)

    print(" ")
    print("Assessing peeling file: " + file_prefix)
    # for i in range(5):
    #     newAcc = (get_marker_accu(new_file[:201, 1:], trueGenotypes[:201, 1:]))
    #     newAcc = round(newAcc, 3)
    #     new_file = new_file[201:, :]
    #     trueGenotypes = trueGenotypes[201:, : ]
    #     print(f"Generation {i + 1}, accuracy: {round(newAcc, 3)}")
    newAcc = get_ind_accu(new_file[:, 1:], trueGenotypes[:, 1:])
    print("Ind Accuracy:", round(newAcc, 3))
    # newAcc = get_gwas_cor(new_file[:, 1:], trueGenotypes[:, 1:])
    # print("Accuracy: ", round(newAcc, 3))



def get_marker_accu(output, real):
    """
    Get correlation between the output and the real data
    """
    
    cors = np.array(
        [np.corrcoef(real[:, k], output[:, k])[0, 1] for k in range(real.shape[1])]
    )
    # if i != 0:
    #     assert cors == []
    return np.nanmean(cors)

def get_ind_accu(output, real):

    cors = np.array(
        [np.corrcoef(real[k, :], output[k, :])[0, 1] for k in range(real.shape[0])]
    )

    return np.mean(cors[400:601])
# assess_peeling_per_generation("peeling.single.estmaf.dosages")

dt = {"names": ("Type", "Population Accu", "Gen1 Accu", "Gen2 Accu", "Gen3 Accu", "Gen4 Accu", "Gen5 Accu"),
                                                  "formats": ("S49", "f4", "f4", "f4", "f4", "f4", "f4")}
accu = np.loadtxt("tests/accu_report.txt", dtype=dt)

mkr_accu = list(filter(lambda x:(x["Type"].decode("UTF-8").split("$")[1] == "Marker_accuracies"), accu))
ind_accu = list(filter(lambda x:(x["Type"].decode("UTF-8").split("$")[1] == "Individual_accuracies"), accu))
sorted_mkr_accu = sorted(mkr_accu, key=lambda x:x["Population Accu"], reverse=True)
sorted_ind_accu = sorted(ind_accu, key=lambda x:x["Population Accu"], reverse=True)

# print(np.array(accu[0]))
# print(type(np.array(accu[0])))

# ntests = accu.shape[0]

# average_accus = {}
# for n, test in enumerate(accu):

#     if n%2 == 0:
#         mkr_accu = 0
#         for gen in range(6):
#             if gen == 0:
#                 mkr_accu += test["Population Accu"]
#             else:
#                 mkr_accu += test[f"Gen{gen} Accu"]
#         mkr_accu /= 6
#         average_accus[test["Type"].decode("UTF-8").split("$")[0]] = mkr_accu
#     else:
#         ind_accu = 0
#         for gen in range(6):
#             if gen == 0:
#                 ind_accu += test["Population Accu"]
#             else: 
#                 ind_accu += test[f"Gen{gen} Accu"]
#         ind_accu /= 6
#         average_accus[test["Type"].decode("UTF-8").split("$")[0]] += ind_accu
#         average_accus[test["Type"].decode("UTF-8").split("$")[0]] /= 2

# sorted_tests = sorted(average_accus.items(), key=lambda x:x[1], reverse=True)
# sorted_accus = sorted(accu, key=lambda x:average_accus[x["Type"].decode("UTF-8").split("$")[0]], reverse=True)
# sorted_accus = sorted(accu, key=lambda x:x[])
# print(average_accus)
# print(sorted_accus)

print("-" * 68 + "Marker Accuracy" + "-" * 68)
columns = ("Type", "Population Accu", "Gen1 Accu", "Gen2 Accu", "Gen3 Accu", "Gen4 Accu", "Gen5 Accu")
format_first_row = "{:<30} " + "{:<20} " * 6
format_row = "{:<30} " + "{:<20.3f} " * 6
print(format_first_row.format(*columns))
for test in sorted_mkr_accu:
    print(format_row.format(
        test["Type"].decode("UTF-8").split("$")[0],
        test["Population Accu"],
        test["Gen1 Accu"],
        test["Gen2 Accu"],
        test["Gen3 Accu"],
        test["Gen4 Accu"],
        test["Gen5 Accu"]
    ))

print("-" * 66 + "Individual Accuracy" + "-" * 66)
columns = ("Type", "Population Accu", "Gen1 Accu", "Gen2 Accu", "Gen3 Accu", "Gen4 Accu", "Gen5 Accu")
format_first_row = "{:<30} " + "{:<20} " * 6
format_row = "{:<30} " + "{:<20.3f} " * 6
print(format_first_row.format(*columns))
for test in sorted_ind_accu:
    print(format_row.format(
        test["Type"].decode("UTF-8").split("$")[0],
        test["Population Accu"],
        test["Gen1 Accu"],
        test["Gen2 Accu"],
        test["Gen3 Accu"],
        test["Gen4 Accu"],
        test["Gen5 Accu"]
    ))