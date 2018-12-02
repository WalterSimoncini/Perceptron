import sys
import random

if len(sys.argv) < 3:
    print("You must provide an output filename and a data set size!")

out_file = open(sys.argv[1] + ".csv", "w")

for i in range(0, int(sys.argv[2])):
    x = random.randint(1, 500)

    function_output = 2 * x + 1
    y = function_output + random.randint(-20, 20)

    if function_output == y:
        continue
    elif function_output > y:
        out_file.write(str(x) + ", " + str(y) + ", " + str(0) + "\n")
    else:
        out_file.write(str(x) + ", " + str(y) + ", " + str(1) + "\n")

out_file.close()