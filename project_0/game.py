import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    ges = int(input("введите число: "))
    if ges < number:
        print("должно быть больше")
    elif ges > number:
        print("должно быть меньше")
    else: 
        print("вы угадали за {} попыток".format(count))
        break

