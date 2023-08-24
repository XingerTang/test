import pytest
import numpy as np

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    print("------------------")

    out = yield
    # print("result", out)

    report = out.get_result()
    with open("tests/summary_report.txt", "a") as file:
        file.write(str(report.sections) + "\n")

    # print("report: %s" % report) 
    # print("stdout: %s" % report.sections)
    # print("step: %s" % report.when)
    # print("nodeid: %s" % report.nodeid)
    # print("description: %s" % str(item.function.__doc__))
    # print("execution result: %s" % report.outcome)


@pytest.hookimpl()
def pytest_terminal_summary(terminalreporter):
    dt = {"names": ("Type", "Population Accu", "Gen1 Accu", "Gen2 Accu", "Gen3 Accu", "Gen4 Accu", "Gen5 Accu"),
                                                  "formats": ("S49", "f4", "f4", "f4", "f4", "f4", "f4")}
    accu = np.loadtxt("tests/accu_report.txt", dtype=dt)

    mkr_accu = list(filter(lambda x:(x["Type"].decode("UTF-8").split("$")[1] == "Marker_accuracies"), accu))
    ind_accu = list(filter(lambda x:(x["Type"].decode("UTF-8").split("$")[1] == "Individual_accuracies"), accu))
    sorted_mkr_accu = sorted(
        mkr_accu, 
        key=lambda x:(x["Population Accu"], x["Gen1 Accu"],x["Gen2 Accu"], x["Gen3 Accu"],x["Gen4 Accu"],x["Gen5 Accu"]), 
        reverse=True
        )
    sorted_ind_accu = sorted(
        ind_accu, 
        key=lambda x:(x["Population Accu"], x["Gen1 Accu"],x["Gen2 Accu"], x["Gen3 Accu"],x["Gen4 Accu"],x["Gen5 Accu"]),
        reverse=True
        )

    terminalreporter.write_sep("-", "Marker Accuracy")
    columns = ("Type", "Population Accu", "Gen1 Accu", "Gen2 Accu", "Gen3 Accu", "Gen4 Accu", "Gen5 Accu")
    format_first_row = "{:<30} " + "{:<20} " * 6
    format_row = "{:<30} " + "{:<20.3f} " * 6
    terminalreporter.write_line(format_first_row.format(*columns))
    for test in sorted_mkr_accu:
        terminalreporter.write_line(format_row.format(
            test["Type"].decode("UTF-8").split("$")[0],
            test["Population Accu"],
            test["Gen1 Accu"],
            test["Gen2 Accu"],
            test["Gen3 Accu"],
            test["Gen4 Accu"],
            test["Gen5 Accu"]
        ))

    terminalreporter.write_sep("-", "Individual Accuracy")
    columns = ("Type", "Population Accu", "Gen1 Accu", "Gen2 Accu", "Gen3 Accu", "Gen4 Accu", "Gen5 Accu")
    format_first_row = "{:<30} " + "{:<20} " * 6
    format_row = "{:<30} " + "{:<20.3f} " * 6
    terminalreporter.write_line(format_first_row.format(*columns))
    for test in sorted_ind_accu:
        terminalreporter.write_line(format_row.format(
            test["Type"].decode("UTF-8").split("$")[0],
            test["Population Accu"],
            test["Gen1 Accu"],
            test["Gen2 Accu"],
            test["Gen3 Accu"],
            test["Gen4 Accu"],
            test["Gen5 Accu"]
        ))