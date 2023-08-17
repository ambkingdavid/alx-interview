#!/usr/bin/python3
"""0-stats"""
import sys
import signal
import re


def print_stat(file_size: int, status_code: dict) -> None:
    """prints the stats to the screen"""
    print(f"File size: {file_size}")
    for key in status_code.keys():
        if status_code[key] > 0:
            print(f"{key}: {status_code[key]}")


def check_input(line: str) -> bool:
    """check valid input"""
    regex = (
            r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
            r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
            r'"GET \/projects\/\d+ HTTP\/1\.1" '
            r'(\d{3}) (\d+)$'
        )

    match = re.match(regex, line)
    if match:
        return True
    return False


def parse_input(line: str, status_code: dict) -> int:
    file_size: int = 0
    """parse the input"""
    if check_input(line):
        line_args = line.split()
        code: int = line_args[-2]
        file_size = int(line_args[-1])

    if code in status_code:
        status_code[code] += 1
        return file_size
    status_code[code] = 1
    return file_size


def signal_handler(sig, frame):
    print_stat(file_size, status_code)
    sys.exit(0)


def main():
    """program entry"""
    num_of_lines: int = 0
    global file_size
    global status_code

    file_size = 0
    status_code = {}

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            file_size += parse_input(line, status_code)
            num_of_lines += 1
            if num_of_lines % 10 == 0:
                print_stat(file_size, status_code)
    except Exception:
        pass


if __name__ == "__main__":
    main()
