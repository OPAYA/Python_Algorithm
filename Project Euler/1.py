num = 0
for i in range(10000):
	if i%3==0 or i%5==0:
		num+=i
print(num)