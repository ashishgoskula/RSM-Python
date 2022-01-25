length = int(input('Enter the train length: '))
speed = int(input('Enter speed of train: '))
man_speed = int(input('Enter speed of man: '))
x = (speed - man_speed)
print('Relative speed in kmph is: ', x)
x = (x * (5 / 18))
time = length / x
print('Time taken by the  train: 1', time)
