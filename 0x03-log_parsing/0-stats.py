#!/usr/bin/env python3
import sys
import datetime


def print_stats(file_size, status_counts):
    print("File size:", file_size)
    for code, count in sorted(status_counts.items()):
        print(code, ":", count)


def parse_line(line):
    parts = line.split()
    if len(parts) < 7:
        return None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = int(parts[-1])
    return ip_address, status_code, file_size


def main():
    file_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            log_data = parse_line(line.strip())
            if log_data is None:
                continue

            ip_address, status_code, size = log_data
            file_size += size

            if status_code.isdigit():
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)


if __name__ == '__main__':
    main()
