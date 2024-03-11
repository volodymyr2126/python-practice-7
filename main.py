from app.io.input import terminal_read, pd_read, file_read
def main():
    first_input = terminal_read()
    second_input = file_read()
    third_input = pd_read()

if __name__ == '__main__':
    main()
