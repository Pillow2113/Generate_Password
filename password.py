import random
seed="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
pwd=''

for i in range(12):
    pwd=pwd+random.choice(seed)
print(f"Password is:{pwd}")

input("按 Enter 以退出...")