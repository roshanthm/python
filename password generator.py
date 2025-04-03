import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


paswd=""

print(".........................password generator..........................")

n = int(input("enter the limit of letters in password:"))
n1 = int(input("enter the limit of symbols in password:"))
n2 = int(input("enter the limit of numbers in password:"))

for i in range(1,n+1):
    char = random.choice(letters)
    paswd+=char
for i in range(1,n1+1):
    char = random.choice(symbols)
    paswd+=char
for i in range(1,n2+1):
    char = random.choice(numbers)
    paswd+=char


s_list = list(paswd)

random.shuffle(s_list)

passwd="".join(s_list)

print("password===",passwd)