lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
target = int(input("Enter the target number: "))
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            print([i, j])
            break