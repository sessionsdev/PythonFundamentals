'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

amount = int(input("How much would you like to invest: $"))

intrest = int(input("What is the intrest rate percentage: %"))

years = int(input("How many years are you investing: "))

earned_intrest = float(intrest / 100) * years * amount

total_amount = earned_intrest + amount

print(f"You will earn ${earned_intrest} in intrest.  Over {years} years, your total investment will be ${total_amount}")
