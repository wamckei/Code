
price_coffee  = int(input("enter the price: "))
discount_of_coffee = int(input("enter the discounted rate: "))

def make_coffee():
    print("Making coffee...")


def discount_apply(price, discount):
    discount = price * (discount / 100)
    final_price = price - discount
    return final_price
5

discounted_price = discount_apply(price_coffee, discount_of_coffee)

print(f"your discounted price is: {discounted_price}")