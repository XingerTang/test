import pytest

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    print("------------------")

    out = yield
    print("result", out)

    report = out.get_result()

    print("report: %s" % report) 
    print("stdout: %s" % report.sections)
    print("step: %s" % report.when)
    print("nodeid: %s" % report.nodeid)
    print("description: %s" % str(item.function.__doc__))
    print("execution result: %s" % report.outcome)
