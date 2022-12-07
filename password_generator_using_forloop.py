import random
letter = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
letters = letter.split(",")
symbols= ['!','@','#','$','%','^','&','*','(',')','?','+','=']
number= "1 2 3 4 5 6 7 8 9 10"
numbers =number.split(" ")                                                                                     #variables declaration EOL

print("Welcome to the password Generator")

num_letters = int(input("How many letters would you like to have in your password: "))
num_symbols = int(input("How many symbols would you like to have in your password: "))
num_numbers = int(input("How many numbers would you like to have in your password: "))                             #inputs EOL

password = ""                                                                                                       #for loop starts
for char in range(1, num_letters+1):
    random_char =random.choice(letters)
    password+= random_char


for sym in range(1, num_symbols+1):
    random_sym = random.choice(symbols)
    password+=random_sym

for num in range(1, num_numbers):
    random_num = random.choice(numbers)
    password+=random_num

print(password)