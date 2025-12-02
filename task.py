import random

print(50 * "-")
print("Basic Password Generator")
print(50 * "-")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]


def rnd_password():
    plen = 1
    while plen < 13:
        for i in random.choice(letters + numbers + symbols):
            print(i, end="")
        if plen == 12:
            break
        plen += 1


rnd_password()
