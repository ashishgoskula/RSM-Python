length = int(input("Enter Train Length: "))
speed = int(input("Enter Man's Speed: "))
time = int(input("Enter time taken: "))
relativespeed = length / time * (18 / 5)
trainspeed = relativespeed + speed
print("The train speed is:", trainspeed)
