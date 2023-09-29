# import pytest
import time
import os
import numpy as np
import platform
import sys
import shutil
from multiprocessing import pool


def read_file_with_rounding(file_path, decimal_place=4):

    with open(file_path, "r") as file:
        values = [line.strip().split() for line in file]

    values = [[row[0]] + [
        str(round(float(data), decimal_place)) for data in row[1:]
    ] for row in values
    ]

    print(values)

read_file_with_rounding("/Users/evie/Lab/Alpha/AlphaPeel/tests/functional_tests/test_rec/outputs/rec.seqfile.seg", 2)