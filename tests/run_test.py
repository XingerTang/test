import subprocess
import platform
# import pytest
import os

linesep = os.linesep

def expand_env_var(var):
    """
    returns the environment variables used with the corresponding os
    """
    system = platform.system()
    if system == "Windows":
        return f"%%{var}%%"
    return f"${var}"

def test_cases():
    command = (
        "for method in a b c d; do"
        + linesep
        + "echo "
        + expand_env_var("method")
        + linesep
        + "done"
        + linesep
        + "echo only"
        )
    
    out = subprocess.run(command, shell=True, capture_output=True, text=True)
    exp = (
        "a"
        + linesep
        + "b"
        + linesep
        + "c"
        + linesep
        + "d"
        + linesep
        + "only"
        + linesep
    )
    assert out.stdout == exp

test_cases()