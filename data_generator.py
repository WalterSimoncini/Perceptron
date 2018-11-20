import sys
import random

if len(sys.argv) < 2:
    print("You must provide an output filename!")

out_file = open(sys.argv[1] + ".csv", "w")

for i in range(0, 1000):
    x = random.randint(1, 500)
    y = random.randint(1, 500)

    if (2 * x + 1) > y:
        out_file.write(str(x) + ", " + str(y) + ", " + str(0) + "\n")
    else:
        out_file.write(str(x) + ", " + str(y) + ", " + str(1) + "\n")

out_file.close()