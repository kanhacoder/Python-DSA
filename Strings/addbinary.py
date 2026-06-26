num1 = "11"
num2 = "1"
num1n = 0
num2n = 0
for i in range(len(num1)):
    num1n += int(num1[len(num1) - 1 - i]) * (2 ** i)
for i in range(len(num2)):
    num2n += int(num2[len(num2) - 1 - i]) * (2 ** i)
result = num1n + num2n
if result == 0:
    print("0")
else:
    listr = []
    while result != 0:
        listr.append(str(result % 2))
        result //= 2
    listr.reverse()
    print("".join(listr))