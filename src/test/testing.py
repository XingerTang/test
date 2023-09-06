import matplotlib.pyplot as plt
import numpy as np

test_single_no_recomb = np.array(
    [0.865, 1.000, 0.884, 0.855, 0.835, 0.697]
)

test_single_estmaf_no_recomb = np.array(
    [0.863, 0.996, 0.882, 0.854, 0.835, 0.697]
)

test_multi_no_recomb = np.array(
    [0.980, 0.996, 0.882, 0.854, 0.835, 0.697]
)

test_multi_estmaf_no_recomb = np.array(
    [0.977, 0.993, 0.941, 0.976, 0.987, 0.989]
)

test_multi_estmaf_esterrors_no_recomb = np.array(
    [0.978, 0.994, 0.943, 0.976, 0.986, 0.990]
)

test_multi_seq_no_recomb = np.array(
    [0.907, 0.797, 0.904, 0.976, 0.992, 0.994]
)

test_multi_estmaf_seq_no_recomb = np.array(
    [0.951, 0.877, 0.920, 0.979, 0.993, 0.994]
)

test_multi_estmaf_esterrors_seq_no_recomb = np.array(
    [0.951, 0.877, 0.920, 0.979, 0.993, 0.994]
)

test_hybrid_single_no_recomb = np.array(
    [0.979, 0.995, 0.948, 0.978, 0.987, 0.989]
)

test_hybrid_single_seq_no_recomb = np.array(
    [0.914, 0.801, 0.923, 0.979, 0.992, 0.994]
)

no_recomb_varname = []
no_recomb = []

# print(no_recomb.shape)
# print(no_recomb)

# fig, ax = plt.subplots()
# ax.bar(no_recomb_varname, no_recomb[:, 0])
# plt.show()

local_var = locals()
local_var_key = local_var.keys()

for item in local_var:
    pass

for vars in local_var_key:
    if vars[:-10] == "_no_recomb":
        no_recomb_varname.append(vars)
        no_recomb.append(local_var[vars])

print(vars)
print(local_var)