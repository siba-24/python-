from collections import Counter

lst = [...]  # لیست ورودی
counts = Counter(lst)

for item in counts:
    print(f'{item} repeats {counts[item]} times.')
