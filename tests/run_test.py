import pytest
import time
import os
import numpy as np
import platform

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
            file.write(" ".join(row) + linesep)

def test_file():  
    system = platform.system()
    subset = np.floor(np.linspace(1, 1000, num=200))
    subset = np.concatenate(([0], subset), dtype=int, casting="unsafe")

    file_r = os.path.join("tests", "peeling.seg")
    seg = read_file(file_r)
    file_w = os.path.join("tests", "seg.subset.txt")
    write_file(file_w, seg[:, subset])

    with open(file_w) as f:
        i = 0
        for line in f:
            if system == "Windows":
                parts = line.strip(os.linesep)
                parts = parts.split()
                i += 1
                print(i)
                parts[0]