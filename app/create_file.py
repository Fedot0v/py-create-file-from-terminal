import sys
import os
from datetime import datetime


def create_directory(path_parts: list) -> str | bytes:
    path = os.path.join(os.getcwd(), *path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(
        file_name: str,
        path: str | os.PathLike | bytes = ".",
        mode: str = "w"
) -> None:
    file_path = os.path.join(path, file_name)
    if os.path.exists(file_path):
        mode = "a"
    with open(file_path, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if mode == "a":
            file.write("\n")
            file.write(f"\n{timestamp}")
        else:
            file.write(f"{timestamp}")

        number_of_line = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line.lower() == "stop":
                break
            file.write(f"\n{number_of_line} {content_line}")
            number_of_line += 1


def main() -> None:
    command = sys.argv
    print(command)
    if "-f" in command and "-d" in command:
        dir_index = command.index("-d")
        file_index = command.index("-f")
        file_name = command[file_index + 1]
        if dir_index < file_index:
            path = create_directory(command[dir_index + 1:file_index])
            create_file(file_name, path)
        else:
            path = create_directory(command[dir_index + 1:])
            create_file(file_name, path)
    elif "-d" in command:
        create_directory(command[2:])
    elif "-f" in command:
        create_file(command[-1])


if __name__ == "__main__":
    main()
