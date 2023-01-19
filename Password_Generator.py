import string as str
import random as rnd
import secrets as scrt

lower_letter=str.ascii_lowercase
upper_letter=str.ascii_uppercase
number=str.digits
special_char=str.punctuation

print("1. lowercase\n2. lowercase + uppercase\n3. lowercase + uppercase + number\n4. lowercase + uppercase + number + character\n")

choice=int(input("Enter choice :"))
while choice < 0 or choice > 4:
    choice=int(input("Ivalid choice \nEnter choice again :"))


if choice == 1:
    alphabet=lower_letter
if choice == 2:
    alphabet=lower_letter+upper_letter
if choice == 3:
    alphabet=lower_letter+upper_letter+number
if choice == 4:
    alphabet=lower_letter+upper_letter+number+special_char

pwd_len=int(input("Enter your password length :"))

while pwd_len<=0:
    print("Invalid size \ntry again")
    pwd_len=int(input("Enter your password length :"))

pwd = ''
for i in range(pwd_len):
  pwd += ''.join(scrt.choice(alphabet))

print(pwd)
