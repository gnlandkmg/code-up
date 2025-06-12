import random

def genPass():
    chr ='abcdefghijklmnopqrstuwxyz0123456789'
    passwd =random.sample(chr,8)
    return passwd

for i in range(3):
    result = genPass()
    print(f"암호 {i+1}: {result}")