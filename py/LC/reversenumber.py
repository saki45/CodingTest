def reversenumber(num):
	if num == 0:
		return num
	sign = 1
	if num < 0:
		num = -num
		sign = -1

	lastdigit, ret = 0,0
	while num > 0:
		lastdigit = num % 10
		num = num // 10
		ret = (ret+lastdigit) * 10

	return (ret//10) * sign

if __name__ == "__main__":

	print(0, reversenumber(0))
	print(1, reversenumber(1))
	print(-1, reversenumber(-1))
	print(100, reversenumber(100))
	print(-24,reversenumber(-24))
