# Exercise 6.5

import os
import time

file = open("Data/stocklog.csv")
file.seek(0, os.SEEK_END)

while True:
    line = file.readline()
    if not line:
        time.sleep(0.1)
        continue
    fields = line.split(",")
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")