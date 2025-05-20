#imports
from time import sleep
#variables
minute = 0
user = input("how long do you wanna work?(in minutes):")
treat = 0
#user introduction
print("terminal pal")
print("This dog gets a treat per minute you work.")
print("   / |__")
print("  (    @|___")
print("  /         O| ")
print(" /   (_____/_| ")
print("/_____/   U U")

while True:
    #the program waits and then prints out a treat and adds to the minute counter and treat
    if str(minute) == user or str(minute) > user:
        treat = treat + 1
        print("0=0")
        break
    sleep(60)
    print("0=0", end="")
    minute = minute +1
    treat = treat + 1
    #this waits till the time the user said is met


print("you did it, you earned the dog ", treat, "treat")
print("   / |__")
print("  (    ^ |___")
print("  /         O| ")
print(" /   (_____/_| ")
print("/_____/   U U")
