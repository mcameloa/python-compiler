
import analyzer

file_data = []


def open_file(path, mode):
    file = open(path, mode)
    return file


def read_file(file):
    content = file.readlines()
    for data in content:
        file_data.append(data)


def main(path):
    global file_data

    file = open_file(path, 'r')
    read_file(file)

    for lex in file_data:
        analyzer.main(lex)


if __name__ == "__main__":
    file_path = input("Enter file path: ")
    main(file_path)
