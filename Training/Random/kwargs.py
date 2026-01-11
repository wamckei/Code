def calc_total(price, delivery_fee = 50):
    total_cost = price + delivery_fee
    return total_cost

total = calc_total(500)
print(total)

total_iteration2 = calc_total(500, 30)
print(total_iteration2)


# *args - *args collects extra positional arguments into a tuple, allowing operations like summing or iterating over them
def add_items(*price):
    total = 0
    for i in price:
        total += i
    print("total is: ", total)


add_items(100, 200, 300)
add_items(60, 70, 80, 90)

###################################

# **kwargs - **kwargs gathers extra keyword arguments (key-value pairs) into a dictionary, useful for handling named options.

def user_profile(**user_info):
    for key, value in user_info.items():
        print("key: ", key, "Value: ", value)


user_profile(name="alice", age=10, city="New York")
user_profile(name="Bob", email="bob@something.com", car="suburu")


