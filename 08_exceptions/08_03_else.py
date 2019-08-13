'''
Write a script that demonstrates a try/except/else.

'''

try:
    num1 = int(input("Please enter a num: "))
    num2 = int(input("Please enter another num: "))
    print(num1 * num2)
except:
    print("Sometihng went wrong")
else:
    print("Else")