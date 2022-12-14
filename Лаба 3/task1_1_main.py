INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE) as file:
        for line in file:
            print(line)
# TODO открыть указатель на файл
         # TODO файл является итератором, который работает с циклом for в построчном режиме


if __name__ == "__main__":
    task()
