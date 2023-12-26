#!/usr/bin/python
print("Content-Type: text/html")    # HTML is following
print()

print("<TITLE>C2IT</TITLE>")
print("<H1>Promouseus C2IT</H1>")

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)