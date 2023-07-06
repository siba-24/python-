birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))

print("Your birth year is:", birth_year)
print("Your birth month is:", birth_month)

year_without_month = birth_year // 100
month_in_year = birth_year % 100

print("Year without month is:", year_without_month)
print("Month in year is:", month_in_year)
            
