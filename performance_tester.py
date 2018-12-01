import subprocess

# Generates a new training set with the specified number of input / output pairs
def generate_training_set (training_set_size):
    subprocess.call(["python", "data_generator.py", "training", str(training_set_size)])

# Runs the linear function classifier and returns the ouput accuracy
def run_program ():
    process = subprocess.Popen(['python', 'linear_function_classifier.py', 'n'], 
                            stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    return process.communicate()[0].rstrip("\n")

out_file = open("performance.csv", "w")

dataset_size = 5

# Test the classifier with variably sized datasets (5 to 500 input/output pairs)
for i in range(0, 100):
    dataset_size = 5 + i * 5
    cumulative_correct_percentage = 0

    # Generate a new training set with the current training size
    generate_training_set(dataset_size)

    # Test the program and collect the averafe accuracy over 10 runs
    for i in range(10):
        program_output = run_program()
        cumulative_correct_percentage += float(program_output)

    average_correct_percentage = cumulative_correct_percentage / 10.0
    out_file.write(str(dataset_size) + ", " + str(average_correct_percentage) + "\n")

    print("Processed data set with size: " + str(dataset_size));