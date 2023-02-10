#!/usr/bin/env python3
from urllib.request import urlopen

with urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt") as res:
    for line in res:
        line = line.decode()
        if line.startswith("datetime"):
            print(line.rstrip())

import smtplib

pass
