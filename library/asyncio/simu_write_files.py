#!/usr/bin/python3.6
# coding=utf-8
# ===============================================================================
#
#         FILE: test.py
#
#        USAGE: ./test.py
#
#  DESCRIPTION:
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: James Zhu (), zhujian0805@gmail.com
# ORGANIZATION: ZJ
#      VERSION: 1.0
#      CREATED: Fri 18 May 2018 09:27:12 AM CST
#     REVISION: ---
# ===============================================================================

import asyncio
import time
import sys

now = lambda: time.time()


async def worker(filename):
    i = 0
    with open(filename, "w") as fh:
        while True:
            i = i + 1
            fh.write("This is the %s line\n" % str(i))
            if i > 10000:
                break

if __name__ == "__main__":
    FILENAME = sys.argv[1]
    count = int(sys.argv[2])
    start = now()
    tasks = []
    for i in range(count):
        fname = "%s%s.txt" % (FILENAME, str(i))
        tasks.append(asyncio.ensure_future(worker(fname)))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('TIME: ', now() - start)
