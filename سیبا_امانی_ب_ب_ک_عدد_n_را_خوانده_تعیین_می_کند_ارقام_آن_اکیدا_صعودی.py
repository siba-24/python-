def check_order(n):
    digits = str(n)
    ascending = True
    descending = True

    for i in range(len(digits)-1):
        if digits[i] > digits[i+1]:
            ascending = False
        if digits[i] < digits[i+1]:
            descending = False

    if ascending:
        return "ارقام اکیدا صعودی هستند"
    elif descending:
        return "ارقام اکیدا نزولی هستند"
    else:
        return "ارقام مرتب نیستند"

n = int(input("عدد را وارد کنید: "))
result = check_order(n)
print(result)
