# Discount-Calculator
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to apply.
    
    Returns:
    - float: The final price after discount if applicable, or the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price < original_price:
    print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")