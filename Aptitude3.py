speed = int(input('Enter speed of train: '))
speed = speed * (5 / 18)
print('Speed of train is: ', speed)
length = int(input('Length of train is: '))
time = int(input('Time taken by train: '))
x = speed * time
print('Distance travelled by the train is: ', x)
bridgelength = x - length
print('Total length of bridge is: ', bridgelength)
