import itertools

# گرفتن لیست از کاربر
lst = input("Enter a list of elements: ").split()

# فشرده کردن و چاپ لیست در هر مرحله
for i in range(1, len(lst)+1):
    compressed_lst = list(itertools.compress(lst, [j < i for j in range(len(lst))]))
    print(compressed_lst)
