__author__ = 'mroot'

import sys, os, math, random, string

os.system('cls' if os.name == 'nt' else 'clear')

while(1):

    input = raw_input("# of dice, # of sides on dice?\n")
    split = input.split(",")

    amount = int(split[0])
    sides = int(split[1])

    rolls = []
    total = 0
    average = 0
    min = 0
    max = 0

    for x in range(amount):
        roll = random.randrange(1, sides+1, 1)
        rolls.append(roll)
        total+=roll

    rolls.sort()

    min = rolls[0]
    max = rolls[-1]
    average = total/amount

    print rolls
    print "Total: "+str(total)
    print "Max: "+str(max)
    print "Min: "+str(min)
    print "Average Roll: "+str(average)
    print "Average Total: "+str(amount*sides/2)

    cont = raw_input("Enter 's' to exit program, anything else to re-roll\n")
    if cont == 's':
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

