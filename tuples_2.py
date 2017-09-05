import re
name = input("Enter file:")
if len(name) < 1: name = "regex_sum_42.txt"
handle = open(name)
y = 0
for line in handle :
	y = y + int(re.findall('0-9]+', line))