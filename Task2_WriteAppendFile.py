# Task 2: Write and append data to a file

# Write user input to file
data = input("Enter data to write to file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

# Append additional data
with open("output.txt", "a") as file:
    file.write("This line is appended to the file.\n")

# Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
