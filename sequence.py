n = int(input("Enter the length of the sequence: "))  # Do not change this line
prev = 0
num = 1
prev1 = 0
prev2 = 0
prev3 = 0
prev4 = 0

for j in range(0, n):

    if j > 6:
        num = num * 2
        num -= prev1

    elif j > 3:
        num = (num) * 2
        prev += 1
        num -= prev

    elif j > 2:
        num = num * 2

    else:
        num = (j + 1)

    prev1 = prev2
    prev2 = prev3
    prev3 = prev4
    prev4 = num

    print(num)