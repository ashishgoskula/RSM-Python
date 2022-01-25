speed = int(input('Enter the train speed: '))
speed = speed * (5 / 18)
print("Train speed: ", speed)
length = int(input('Enter length of train: '))
platform = int(input('Enter length of platform: '))
distance = length + platform
print("Total distance is: ", distance)
time = (distance / speed)
print("Time taken to cross the platform: ", time)
