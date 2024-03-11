from app.io.input import terminal_read, pd_read, file_read
from app.io.output import terminal_write, file_write


def main():
    input_file = "data/test.txt"
    file_for_pandas = "data/simple.csv"
    outputs = "data/outputs.txt"
    first_input = terminal_read()
    second_input = file_read(input_file)
    third_input = pd_read(file_for_pandas)
    terminal_write(first_input)
    file_write(outputs, first_input)
    terminal_write(second_input)
    file_write(outputs, second_input)
    terminal_write(third_input)
    file_write(outputs, third_input)


if __name__ == '__main__':
    main()
