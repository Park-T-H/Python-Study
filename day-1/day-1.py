# "", ''
print("Hello World! 'Hello World!'")
print('Hello World! "Hello World!"')

# 줄 출력 1
print("1. Mix 500g of Flour, 10g Yeastand 300ml Water in a bowl.")
print("2. knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# 줄 출력 2
print("1. Mix 500g of Flour, 10g Yeastand 300ml Water in a bowl.\n2. knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")

# 입출력
print("Hello " + input("What is your name? "))
# What is your name? 태형
# Hello 태형

# 문자열 길이 1
name = input()
numOfLetters = len(name)
print(numOfLetters)

# 문자열 길이 2
print(len(input()))

# 변수 임시 저장
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = a
a = b
b = c
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# 밴드명 생성기
#1. Create a greeting for your program.
print("밴드명 생성기")
#2. Ask the user for the city that they grew up in.
city = input("너가 태어난 곳은 어디니?\n")
#3. Ask the user for the name of a pet.
pet = input("너의 애완동물 이름은 무엇이니?\n")
#4. Combine the name of their city and pet and show them their band name.
print("너의 밴드명은 " + city + " " + pet)
#5. Make sure the input cursor shows on a new line..
