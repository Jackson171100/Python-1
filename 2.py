import random 
num=random.randint(1,100168723)
Wrongcount=0
while True:
    a=input("give me a number 1-100,168,723")
    if num==a:
        print("congrats")
        break
    else:
        Wrongcount+=1
    if Wrongcount==5:
        z=input("cheat mode unlocked use yes or no.")
        if z=="yes":
            for i in range(num):
                print(i+1)
            print("congrats")
            break
        print("game over")
        break
            