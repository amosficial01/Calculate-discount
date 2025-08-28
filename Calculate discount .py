 # The calculate_discount function takes the price and discount_percent as parameters.
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to be applied.

    Returns:
        float: The final price after the discount, or the original price if no discount is applied.
    """
    # Check if the discount is 20% or higher.
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        # If the discount is less than 20%, return the original price.
        return price

# Main program block to prompt the user and print the result.
def main():
    """
    Prompts the user for price and discount, and prints the final price.
    """
    try:
        # Prompt the user to enter the original price.
        original_price = float(input("Enter the original price of the item: "))
        # Prompt the user to enter the discount percentage.
        discount_percentage = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percentage)

        # Check if the final price is different from the original price to determine if a discount was applied.
        if final_price < original_price:
            print(f"The final price after the discount is: ${final_price:.2f}")
        else:
            print(f"No discount was applied. The price remains: ${final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number for price and discount.")

# Run the main function.
if __name__ == "__main__":
    main()
