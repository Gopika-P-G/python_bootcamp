
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



combined_string = name1 + name2
ls = combined_string.lower()

t = ls.count('t')
r = ls.count('r')
u = ls.count('u')
e = ls.count('e')
true = t+r+u+e

l = ls.count('l')
o= ls.count('o')
v = ls.count('v')
e = ls.count('e')
love = l+o+v+e

score = str(true)+str(love)
score =(int(score))
if score < 10 or score> 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"your score is {score}")