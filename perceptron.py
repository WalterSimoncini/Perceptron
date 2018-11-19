import time 
import random

line_separator = "\n------------------------------------------------------------------\n"

learning_constant = 0.1

# Targets and inputs for the OR function
# targets = [0, 1, 1, 1] 
# inputs = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

targets = [0, 0, 0, 1]
inputs = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

weights = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]

sum_error = 1000
# prev_error_sum = error_sum
# is_error_decreasing = True

def activation_function (value):
        if value > 0:
            return 1
        else:
            return 0

print "Random weights: " + str(weights) + line_separator

epoch = 1
while sum_error > 0:
    sum_error = 0.0

    for i in range(0, len(targets)):
        t = targets[i]
        output = inputs[i][0] * weights[0] + inputs[i][1] * weights[1] + inputs[i][2] * weights[2]

        activation = activation_function(output)
        error = t - activation

        sum_error += abs(error)

        for j in range(0, len(weights)):
            delta = learning_constant * error * inputs[i][j]
            weights[j] += delta

        print "Target: " + str(t) + " - Ouput: " + str(activation) + " - " + str(weights)
    
    print("\nEpoch " + str(epoch) + " with error sum: " + str(sum_error) + line_separator)
    
    time.sleep(1)
    epoch += 1