x1, y1 = map(int, input('Enter the x and y coordinates of camera 1: ').split())
x2, y2 = map(int, input('Enter the x and y coordinates of camera 2: ').split())
x3, y3 = map(int, input('Enter the x and y coordinates of camera 3: ').split())

# محاسبه مرکز مستطیل
center_x = (min(x1, x2, x3) + max(x1, x2, x3)) / 2
center_y = (min(y1, y2, y3) + max(y1, y2, y3)) / 2

# محاسبه طول بردارهای قائم الزاویه‌ی مرکز مستطیل
length1 = ((x1 - center_x)**2 + (y1 - center_y)**2)**0.5
length2 = ((x2 - center_x)**2 + (y2 - center_y)**2)**0.5
length3 = ((x3 - center_x)**2 + (y3 - center_y)**2)**0.5

# محاسبه طول قطر مستطیل
diagonal = ((max(x1, x2, x3) - min(x1, x2, x3))**2 + (max(y1, y2, y3) - min(y1, y2, y3))**2)**0.5

# محاسبه فاصله‌ی دوربین چهارم تا مرکز مستطیل
distance_4 = (diagonal**2 - ((max(length1, length2, length3) + min(length1, length2, length3)) / 2)**2)**0.5

# محاسبه مختصات دوربین چهارم
x4 = center_x
y4 = center_y + distance_4

# چاپ خروجی
print('The coordinates of camera 4 are: ({}, {})'.format(x4, y4))
