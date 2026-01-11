#innefficient way - creating a huge list in memory
squares = []
for i in range(1, 10000001):
    squares.append(i * i)

print("Total squares: " , len(squares))



# Memory-efficient way using a generator

def generator_squares():
    for i in range(1, 10000001):
        yield i * i

squares = generator_squares()

# Get the first five squares

for _ in range(5):
    print(next(squares))
    print(next(squares))


# Use tuple's for more memory efficient data collections if there isn't a need to change the data - they are immutable