length = int(input("Enter Train Length: "))
speed = int(input("Enter Man's Speed: "))
time = int(input("Enter time taken: "))
relative_speed = length / time * (18 / 5)
train_speed = relative_speed + speed
print("The train speed is:", train_speed)
