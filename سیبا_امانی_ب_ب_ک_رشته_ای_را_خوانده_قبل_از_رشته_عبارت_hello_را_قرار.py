string1 = input("Enter a string: ")
string1 = "hello" + string1

n = int(input("Enter the value of n: "))
char_n = string1[n]

string2 = input("Enter another string: ")
if string2 in string1:
    print("The second string exists in the first one.")

m = int(input("Enter the value of m: "))
print(string1[n:m+1])
