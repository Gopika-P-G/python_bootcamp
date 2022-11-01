input("Welcome to Treasure Island \n Your Mission is to Find the Treasure")
direction =input("where you want to go left or right: ")

if direction == "left":
    travel = input("do you want to wait for boat or prefer to swim: ")

    if travel== "boat":
        place = input("which place would you choose to walk forest or mountain: ")


        if place == "forest":
            door =input("which door do you choose green,yellow or blue: ")


            if door == " yellow":
                print("you found the treasure room filled with rubygems")

            elif door == "green":
                print("You found the Treasure room filled with donkey")

            else: 
                print("game over you release the fire dragon")
        else:
            print("please jump from mountain to exit")


    else:
        print("Eaten by shark")


else:
    print("game over you fell in to lava")


