# Writing to a new file
with open("new_file.txt", "w") as f:
    f.write("Hello! This file was created using Python.")

print("File 'new_file.txt' has been created successfully.")

# Reading from the file
with open("new_file.txt", "r") as f:
    content = f.read()
    print(f"Content of the file: {content}")
