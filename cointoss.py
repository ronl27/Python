import random
import math

def cointoss():

    count = 0
    head_count = 0
    tail_count = 0

    while count <= 5000:
        num = random.randint(0,1)
        print num
        if num == 1:
            head_count += 1
            print "You got heads! So far you have gotten heads", head_count, "times!"
        if num == 0:
            tail_count += 1
            print "You got tails! So far you have gotten tails", tail_count, "times!"
        count += 1

cointoss()
