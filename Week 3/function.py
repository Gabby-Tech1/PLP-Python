## Question 1
def calculate_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    
    if discount_percent >= 20:
        return price - discount
    return price


## Question 2
original_price = float(input("Enter the price: "))
discount_percentage = float(input("Enter the discount percent: "))
result = float(calculate_discount(original_price, discount_percentage))
print(result)