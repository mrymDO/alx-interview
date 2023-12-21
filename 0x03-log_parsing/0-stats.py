#!/usr/bin/python3
"""Log parsing"""

import sys
import re

total_file_size = 0

status_code_count = {
    200: 0, 301: 0, 400: 0,
    401: 0, 403: 0, 404: 0,
    405: 0, 500: 0
}

pattern = re.compile(
    r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] '
    r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
)

try:
    for line in sys.stdin:
        match = pattern.match(line.strip())

        if match:
            ip_adress, date, status_code, file_size = match.groups()
            total_file_size += int(file_size)
            status_code_count[int(status_code)] += 1

            if total_file_size % 10 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(status_code_count):
                    print(f"{code}: {status_code_count[code]}")
                print()
except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count):
        print(f"{code}: {status_code_count[code]}")
