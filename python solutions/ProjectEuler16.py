# What is the sum of the digits of the number 21000?
summer = 0
num = str(2**1000)
array = num[::1]
print(array)
print(len(array))
for i in range(0, len(array)):
    summer += int(array[i])
print(summer)


