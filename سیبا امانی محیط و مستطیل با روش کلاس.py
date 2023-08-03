class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# خواندن طول و عرض از کاربر
length = float(input("طول مستطیل را وارد کنید: "))
width = float(input("عرض مستطیل را وارد کنید: "))

# ایجاد یک شیء از کلاس Rectangle با استفاده از طول و عرض وارد شده
rectangle = Rectangle(length, width)

area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print(f"مساحت مستطیل: {area}")
print(f"محیط مستطیل: {perimeter}")
