import random

random_interger = random.randint(10, 100)
print(random_interger)

# Prints a random fp number between 0.0 & 1.0
ran_num = random.random()
print(ran_num)

# If we use random and multiple it by "something" say for instance 10, it will create a random FP number between 0 and 10 etc, recomended option
ran_num = random.random() * 10
print(ran_num)

# Another option is to use the uniform option
ran_fp = random.uniform(15, 209)
print(ran_fp)

# Heads or Tails.
print(" This starts the heads or tails chance ")
print("........................................")

x = random.randint(1, 2)
if x == 1:
    print(x)
    print("Heads")
else:
    print(x)
    print("Tails")