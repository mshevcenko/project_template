from app.io.input import read_text_from_terminal, read_text_from_file, read_csv_from_file_with_pandas
from app.io.output import write_text_to_terminal, write_text_to_file


def main():
    text_from_terminal = read_text_from_terminal("Write some text: ")
    text_from_file = read_text_from_file("data/test.txt")
    data_from_csv = read_csv_from_file_with_pandas("data/test.csv")
    text_from_csv = str(data_from_csv.to_dict())
    write_text_to_terminal(text_from_terminal)
    write_text_to_terminal(text_from_file)
    write_text_to_terminal(text_from_csv)
    write_text_to_file(text_from_terminal, "data/text_from_terminal.txt")
    write_text_to_file(text_from_file, "data/text_from_file.txt")
    write_text_to_file(text_from_csv, "data/text_from_csv.txt")


if __name__ == "__main__":
    main()
