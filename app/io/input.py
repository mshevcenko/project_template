import pandas as pd


def read_text_from_terminal(placeholder="Write text:"):
    """Reads text from terminal

    Args:
        placeholder (str): text, which will be printed before input. Default value is "Write text:"

    Returns:
        str. Text from terminal
    """
    return input(placeholder)


def read_text_from_file(filepath):
    """Reads all text from file

    Args:
        filepath (str): path to file

    Returns:
        str. Text from file
    """
    with open(filepath, "r") as file:
        return file.read()


def read_csv_from_file_with_pandas(filepath):
    """Reads all text from csv file using pandas

    Args:
        filepath (str): path to file

    Returns:
        pandas.DataFrame. data from csv file like pandas.DataFrame object
    """
    return pd.read_csv(filepath)
