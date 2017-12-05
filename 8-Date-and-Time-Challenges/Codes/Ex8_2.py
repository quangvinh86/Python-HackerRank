#!/usr/bin/env python3
from datetime import datetime

def time_delta(t1, t2):
    j1 = t1.split()
    j2 = t2.split()
    s1 = j1[0]+":"+j1[1]+":"+j1[2]+":"+j1[3]+":"+j1[4]+":"+j1[5]
    s2 = j2[0]+":"+j2[1]+":"+j2[2]+":"+j2[3]+":"+j2[4]+":"+j2[5]
    FMT = '%a:%d:%b:%Y:%H:%M:%S:%z'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    return int(abs(tdelta.total_seconds()))


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
