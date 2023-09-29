import numpy as np
import matplotlib.pyplot as plt
import operator

# def read_file(file_path, **kwargs):
#     """
#     INPUT:
#     file_path: str, the path of the file to be read
#     decimal_place(optional): if provided, round the data with the given
#     decimal places
#     OUTPUT:
#     values: 2d list of str, store the values of the records
#     """
#     with open(file_path, "r") as file:
#         values = [line.strip().split() for line in file]

#     if "decimal_place" in kwargs.keys():
#         # round the data if data exists
#         values = [
#             [line[0]]
#             + [round(float(data), kwargs["decimal_place"]) for data in line[1:]]
#             if line
#             else line
#             for line in values
#         ]
#     else:
#         # convert data to float for comparison if data exists
#         values = [
#             [line[0]] + [float(data) for data in line[1:]] if line else line
#             for line in values
#         ]

#     return values


# geno_w_missing = read_file("/Users/evie/Lab/Alpha/AlphaPeel/tests/accuracy_tests/baseData/genotypes.txt")
# geno_true = read_file("/Users/evie/Lab/Alpha/AlphaPeel/tests/accuracy_tests/baseData/trueGenotypes.txt")


# geno_accu = [0] * 5


# for gen in range(5):
#     count = 0
#     for num in range(200):
#         id = gen * 200 + num
#         for locus in range(1000):
#             if geno_w_missing[id][locus + 1] == 9:
#                 count += 1

#     geno_accu[gen] = 1 - (count / (200 * 1000))


# print(geno_accu)

columns = (
        "Type",
        "Population Accu",
        "Gen1 Accu",
        "Gen2 Accu",
        "Gen3 Accu",
        "Gen4 Accu",
        "Gen5 Accu",
    )
dt = {"names": columns, "formats": ("S53", "f4", "f4", "f4", "f4", "f4", "f4")}
accu = np.loadtxt("/Users/evie/Lab/Alpha/AlphaPeel/tests/accuracy_tests/accu_report.txt", dtype=dt)

mkr_accu = list(
        filter(
            lambda x: (x["Type"].decode("UTF-8").split("$")[1] == "Marker_accuracies"),
            accu,
        )
    )

ind_accu = list(
        filter(
            lambda x: (
                x["Type"].decode("UTF-8").split("$")[1] == "Individual_accuracies"
            ),
            accu,
        )
    )

sorted_mkr_accu = sorted(
        mkr_accu, key=operator.itemgetter(*columns[1:]), reverse=True
    )

sorted_ind_accu = sorted(
        ind_accu, key=operator.itemgetter(*columns[1:]), reverse=True
    )


fig, ax = plt.subplots(1, 2)

accu_list = [mkr_accu, ind_accu]
accu_name_list = ["marker accuracy", "individual accuracy"]

for i in range(2):
    current_accu = accu_list[i]
    accu_name = accu_name_list[i]
    for test in current_accu:
        ax[i].plot([test["Gen1 Accu"],
                    test["Gen2 Accu"],
                    test["Gen3 Accu"],
                    test["Gen4 Accu"],
                    test["Gen5 Accu"]], "-.", label = test["Type"].decode("UTF-8").split("$")[0][5:])
        
    ax[i].set_xticklabels([f"Gen{gen + 1}" for gen in range(5)])
    ax[i].set_xticks([0, 1, 2, 3, 4])
    ax[i].set_xlabel("generations")
    ax[i].set_ylabel("accuracy")
    ax[i].set_title(accu_name)
    ax[i].legend()


plt.show()

# fig, ax = plt.subplots()

# accu_dict = {}
# test_name_list = []
# for test in mkr_accu:
#     test_name_list.append(test["Type"].decode("UTF-8").split("$")[0][5:])

# accu_dict["marker accuracy"] = []
# for test in mkr_accu:
#     accu_dict["marker accuracy"].append(test["Population Accu"])

# accu_dict["individual accuracy"] = []
# for test in ind_accu:
#     accu_dict["individual accuracy"].append(test["Population Accu"])

# x = np.arange(len(accu_dict["marker accuracy"]))
# width = 0.4
# multiplier = 0

# for test_type, accuracies in accu_dict.items():
#     offset = width * multiplier
#     rects = ax.bar(x + offset, accuracies, width, label=test_type)
#     ax.bar_label(rects)
#     multiplier += 1

# ax.set_ylabel("Accuracy")
# ax.set_xlabel("Test")
# ax.set_title("Accuracies for different tests")
# ax.set_xticks(x + width)
# ax.set_xticklabels(test_name_list)
# ax.set_ylim([0.825, 1])
# ax.legend()

# plt.show()