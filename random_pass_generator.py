import random
print("Password generator")
passlen = int(input("Enter your pass length: "))
base = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?][}{;/.<>|\-_=+"
while passlen > len(base):
    print ("---ALERT--- Max length is 90 signs ---ALERT--- ")
    passlen = int(input("Enter a smaller number: "))
res =  "".join(random.sample(base,passlen ))
print ("Your randomly generated password is: ", res)