import random
r = random

color_list = ['красный','синий','оранжевый','желтый','зеленый','фиолетовый','коричнивый','серый','черный','голубой']
elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
monetka_list = ['Орел','Решка']

def gen_pass8():
    passlen = 8
    password = ""


    for i in range(passlen):
        password += r.choice(elements) # Добовление символов`
    return password
def monetka():
    return r.choice(monetka_list)
def gen_pass16():
    passlen = 16
    password = ""


    for i in range(passlen):
        password += r.choice(elements) # Добовление символов`
    return password
def rnum():
    return r.choice([1,2,3,4,5,6,7,8,9,0,10])
def color():
    return r.choice(color_list)