def fact(n):
    f = 1

    for x in range(1, n +1):
        f *= x

    return f
n = int(input())
for i in range(n) :
	k = int(input())
	k -= 1
	p = fact(k)
	print(p+1)