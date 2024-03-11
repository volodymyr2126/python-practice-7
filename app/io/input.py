import pandas as pd


def terminal_read() -> str:
    """
    Reads text from terminal
    :return (str): string of text read from terminal
    """
    res = input("Enter text: ")
    return res


def file_read(file_name) -> str:
    """
    Reads text from file.
    :param file_name (str): name of file to read
    :return (str): Text from file
    """
    with open(file_name, "r") as file:
        res = file.read()
    return res


def pd_read(file_name):
    """
    Reads text from file using pandas library.
    :param file_name (str): name of file to read
    :return (str): Information from file
    """
    res = pd.read_csv(file_name)
    return res
