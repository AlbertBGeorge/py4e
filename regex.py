import re
name = input('Enter file:')
if len(name) < 1 : name = "regex_sum_17868.txt"
handle = open(name)
sum = 0
nums = list()
for line in handle :
	nums = re.findall('[0-9]+', line)
	if len(nums) > 0 :
		for num in nums :
			sum += int(num)

print(sum)