#!/usr/bin/env python3
import os
import sys


def framer(filepath, file_size, file_content):
    # Frame and write file information and content
    sys.stdout.buffer.write(f"{filepath}\n{file_size}\n".encode())
    sys.stdout.buffer.write(file_content)
    sys.stdout.buffer.write("\n".encode())  # Delimiter


def unframer():
    # Read framed data from stdin
    while True:
        file_name = sys.stdin.buffer.readline().decode().strip()
        if not file_name:
            break
        file_size = int(sys.stdin.buffer.readline().decode().strip())
        file_content = sys.stdin.buffer.read(file_size)
        yield file_name, file_content
        sys.stdin.buffer.readline()  # Remove delimiter


def create_archive(paths):
    # Process only file paths
    for path in paths:
        if os.path.isfile(path):
            with open(path, "rb") as f:
                file_size = os.fstat(f.fileno()).st_size
                file_content = f.read()
                framer(path, file_size, file_content)
        else:
            sys.stderr.write(f"Error: {path} is not a file\n")


def extract_archive():
    for file_name, content in unframer():
        # Write file content
        with open(file_name, "wb") as f:
            f.write(content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Invalid usage. Use 'c' for create or 'x' for extract.\n")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "c":
        files = sys.argv[2:]
        create_archive(files)
    elif mode == "x":
        extract_archive()
    else:
        sys.stderr.write("Invalid mode. Use 'c' for create or 'x' for extract.\n")
