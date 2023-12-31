#!/usr/bin/python3
"""0-stats"""
import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
code_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        if len(data) > 6:
            status_code = int(data[-2])
            file_size = int(data[-1])
            if status_code in code_count:
                code_count[status_code] += 1
                total_size += file_size
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(code_count.keys()):
                if code_count[code] > 0:
                    print("{}: {}".format(code, code_count[code]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code in sorted(code_count.keys()):
        if code_count[code] > 0:
            print("{}: {}".format(code, code_count[code]))
