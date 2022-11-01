age = input("What is your current age?")
years_remaining = 80 - int(age)
month_remaining = years_remaining * 12
week_remaining  = years_remaining *52
days_remaining  = years_remaining *365
print(f"You have {days_remaining} days, {week_remaining} weeks, and {month_remaining} months left.")