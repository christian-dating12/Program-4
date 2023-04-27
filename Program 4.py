# Christian M. Dating | BSCPE 1-5

# Write a method in python that will create two separate text files after reading the source text files named
# integers.txt that contains 20 integers. The first output file will be named double.txt containing the square
# of all even integers found in integers.txt and the second file will be named triple.txt containing the cube of
# all odd numbers found in the integers.txt.

input("\n\033[94mPress Any Key to Start...")
print("\033[90m=" * 80)

# Intro
import pyfiglet
greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "Thin"))

# Pseudocode
# define squared, define cube
def squared(i):
    squ = int(i) ** 2
    return squ

def cube(i):
    cub = int(i) ** 3
    return cub

import random
even = []
odd = []
# open integers.txt (write)
with open("integers.txt", "w") as f:
    for i in range(20):
        num = random.randint(1,20)
        f.write(str(num) + "\n")
# read integers.txt per lines
# even or odd
# open double.txt (write)
# if even, write double.txt
# open triple.txt (write)
# if odd, write triple.txt
# START