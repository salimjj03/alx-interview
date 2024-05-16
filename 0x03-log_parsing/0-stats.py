#!/usr/bin/python3

import sys
import signal


def result(ls, sum):
    print("File size: {}".format(sum))
    for i in sorted(ls.keys()):
        if ls[i] > 0:
            print("{}: {}".format(i, ls[i]))


status_code = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}
count = 0
sum = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            result(status_code, sum)

        count += 1

        try:
            sum += int(line.split()[-1])
        except Exception:
            pass

        try:
            if line.split()[-2] in status_code:
                status_code[line.split()[-2]] += 1
        except Exception:
            pass
    result(status_code, sum)

except KeyboardInterrupt:
    result(status_code, sum)
    raise
