def  calculate_discount(price, discount_percent):
    price = int(input("Enter the price: "))
    discount_percent = int(input('Enter the discount amount without percent sign: '))
    if discount_percent >= 20:
        result = price - (price * (discount_percent / 100))
        return result
    else:
        return price


print(calculate_discount(0,0))