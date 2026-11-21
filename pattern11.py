    # *
    # * *
    # *   *
    # *     *
    # * * * * *


for i in range(5):
    if i == 0:
        print("*")
    elif i == 4:
        print("* " * 5)
    else:
        print("*" + " " * (2 * i - 1) + "*")