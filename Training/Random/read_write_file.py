# Write to a file with context manager (auto opens and closes connections)
with open('1.txt', 'w') as file:
    file.write("just some data  \n")

# Append to a file with context manager (auto opens and closes connections)
with open('1.txt', 'a') as file:
    file.write("Adding some additional data....  \n")
    

# Read to a file with context manager (auto opens and closes connections)
with open('1.txt', 'r') as file:
    content = file.read()

print(content)
