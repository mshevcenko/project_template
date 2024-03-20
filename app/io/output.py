import pandas as pd


def write_text_to_terminal(text):
    """Writes text to terminal

    Args:
        text (str): text, which will be printed to terminal

    Returns:
        None
    """
    print(text)


def write_text_to_file(text, filepath):
    """Writes text to file

    Args:
        text (str): text, which will be printed to file
        filepath (str): path to file

    Returns:
        int. Number of characters, which were written to file
    """
    with open(filepath, "w") as file:
        return file.write(text)


def write_csv_to_file_with_pandas(df, filepath):
    """Writes dataframe to csv file

    Args:
        df (pandas.DataFrame): dataframe, which will be printed to file
        filepath (str): path to file

    Returns:
        None
    """
    df.to_csv(filepath)
