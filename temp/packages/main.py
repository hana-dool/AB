"""
module docstring
"""


def custom_function(var1: list, var2: float) -> float:
    """[summary]

    Args:
        x (list): [description]
        y (float): [description]

    Returns:
        [type]: [description]
    """
    return var1 ** 2 + var2


def setup_line(var1, var2):
    """[summary]
    Args:
        var1 ([type]): [description]
        var2 ([type]): [description]
    """
    if var1 + var2 == 1:
        print(3)
    else:
        print(4)
