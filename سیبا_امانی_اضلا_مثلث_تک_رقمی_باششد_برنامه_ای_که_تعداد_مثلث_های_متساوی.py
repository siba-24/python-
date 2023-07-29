count = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a + b >= c and b + c >= a and a + c >= b:
                print(f"مثلث متساوی الساقین با اضلاع {a}, {b}, {c}")
                count += 1

print(f"تعداد کل مثلث های متساوی الساقین: {count}")
