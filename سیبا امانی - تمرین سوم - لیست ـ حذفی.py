n = int(input("Please enter n: "))
lst = []
while True:
    num = int(input("Please enter a number: "))
    if num == n:
        break
    elif num < n:
        lst.append(num)
print(lst)
