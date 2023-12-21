#!/usr/bin/python3
"""Log parsing"""

import re
import sys
import traceback


def parse_log_entries():
    """log parsing"""

    total_file_size = 0
    lines_processed = 0
    status_code_count = {
        '200': 0, '301': 0, '400': 0,
        '401': 0, '403': 0, '404': 0,
        '405': 0, '500': 0
    }

    try:
        for line in sys.stdin:
            match = re.match(
                r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] '
                r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
                line.strip()
            )

            if match:
                ip_address, date, status_code, file_size = match.groups()
                total_file_size += int(file_size)
                status_code_count[status_code] += 1

                lines_processed += 1
                if lines_processed % 10 == 0:
                    print(f"File size: {total_file_size}")
                    for code in sorted(status_code_count):
                        if status_code_count[code] > 0:
                            print(f"{code}: {status_code_count[code]}")

    except KeyboardInterrupt:
        pass
    except BrokenPipeError:
        pass
    finally:
        print(f"File size: {total_file_size}")
        for code in sorted(status_code_count):
            if status_code_count[code] > 0:
                print(f"{code}: {status_code_count[code]}")


if __name__ == "__main__":
    parse_log_entries()
