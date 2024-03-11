import pandas as pd
import pandas.errors


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
    try:
        with open(file_name, "r") as file:
            res = file.read()
    except FileNotFoundError:
        return "Error"
    return res


def pd_read(file_name):
    """
    Reads text from file using pandas library.
    :param file_name (str): name of file to read
    :return (pandas.DataFrame): Information from file
    """
    try:
        res = pd.read_csv(file_name)
    except FileNotFoundError:
        return "Error"
    except pandas.errors.EmptyDataError:
        return "Empty file"
    return res
