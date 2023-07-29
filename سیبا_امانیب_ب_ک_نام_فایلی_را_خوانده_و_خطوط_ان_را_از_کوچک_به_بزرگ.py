# نام فایل را از ورودی دریافت می‌کنیم
filename = input("لطفاً نام فایل را وارد کنید: ")

# لیست خطوط را تعریف می‌کنیم
lines = []

# فایل را باز می‌کنیم و خطوط را به لیست اضافه می‌کنیم
with open(filename, 'r') as file:
    for line in file:
        lines.append(line.strip())

# خطوط را به صورت الفبایی مرتب می‌کنیم
sorted_lines = sorted(lines)

# خروجی را نمایش می‌دهیم
for line in sorted_lines:
    print(line)
