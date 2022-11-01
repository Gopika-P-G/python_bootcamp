print(input("Welcome to the tip calculator"))
total_bill = input ("What was the total bill?")
percent_of_tip=input("What percet of tip would you like to give? 10 12 or 15?")

bill_split = input("How many people to split the bill ?")
tips = float(total_bill) * (float(percent_of_tip)/100)
bill = float(total_bill) + (1.0+ tips)
bill_per_person = float(total_bill)/int(bill_split)
your_total_bill = round(bill,2)

print(f'Each person should pay: {bill_per_person}')
print(f"Thank you for coming Your  bill is  {your_total_bill }")