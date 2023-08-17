#!/usr/bin/python3
"""0-stats"""
import re
from collections import defaultdict


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
code_count = defaultdict(int)
total_size = 0
line_count = 0

pattern = r'^(?P<ip>\S+) - \[(?P<date>.+)\] "(?P<method>\S+) \
  (?P<path>\S+) (?P<protocol>\S+)" (?P<status_code>\d+) \
    (?P<file_size>\d+)$'

try:
    for line in sys.stdin:
        line_count += 1
        match = re.search(pattern, line)
        if match:
            status_code = int(match.group('status_code'))
            file_size = int(match.group('file_size'))
            code_count[status_code] += 1
            total_size += file_size
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(code_count.keys()):
                if code in status_codes:
                    print("{}: {}".format(code, code_count[code]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code in sorted(code_count.keys()):
        if code in status_codes:
            print("{}: {}".format(code, code_count[code]))
