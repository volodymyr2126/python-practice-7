def terminal_write(content) -> None:
    """
    Writes content to terminal
    :param content (Any): content to write
    :return: None
    """
    print("This is terminal output:\n")
    print(str(content) + "\n\n")
    return None


def file_write(file_name, content) -> None:
    """
    Writes content to specified file
    :param file_name (str): name of the file to write to
    :param content (Any): content to write
    :return: None
    """
    with open(file_name, "a") as file:
        file.write(str(content) + "\n\n")
    return None
