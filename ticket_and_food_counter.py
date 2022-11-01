from multiprocessing.sharedctypes import Value


height = int(input("Enter your height:"))
age  = int(input (" enter your age:"))
photo = input("Do you need a picture yes or no:")
food =input("do you like to have food yes or no :")
dictionary ={'pizza':3 , 'muffin':2, 'cc':5, 'milk':2}
def get_price(age):
    if age <= 12:
        print("your ticket is :$5")
        return 5
    elif age > 12 and age <= 18:
        print("your ticket is $7")
        return 7
    else:
        print('your ticket is 12$')
        return 12

def get_photo_price(photo):
    if photo == "yes":
        print(f"your photo costs is:3$")
        return 3
    else:
        return 0
def get_food(food):
    return dictionary.get(food, 0)
    # #if food in dictionary:
    #     return dictionary[food]
    # else:
    #     0


if height >= 120:
    print("you can ride the roller coaster!")
    price = get_price(age)
    photo_price = get_photo_price(photo)
    snack= get_food(food)
    
    
    print(f"your snack price is:{snack}")
    print(f'your total bill is:{price+ photo_price+snack}')

else:
    print(" sorry you cant ride")

