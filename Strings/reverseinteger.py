def reverseInt():
    int1 = int(input("Enter any integer: "))
    negative = int1 < 0
    digits = str(abs(int1))
    reversed_digits = digits[::-1]
    if len(reversed_digits) > 32:
        return 0
    result = int(reversed_digits)
    return -result if negative else result

print(reverseInt())