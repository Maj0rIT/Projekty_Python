import random

male = "qwertyuiopasdfghjklzxcvbnm"
duze = "QWERTYUIOPASDFGHJKLZXCVBNM"
liczby = "1234567890"
znaki = "[]{}()*;/,._-"

wszystko = male + duze + liczby + znaki
ilosc = 16
haslo = "".join(random.sample(wszystko,ilosc))

print(haslo)

input()