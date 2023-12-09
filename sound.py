import winsound
from random import randint

def make_cake():
    start = 22
    while start > 0:
        winsound.Beep(randint(50, 2000), randint(200, 1000))
        start -= 1

make_cake()