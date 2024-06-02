# Function to calculate the tip of the ordered food
def calculate_tip(food_charge):
    return food_charge * 0.18

# Function to calculate the sales tax of the ordered food
def calculate_sales_tax(food_charge):
    return food_charge * 0.07

# Main function to calculate the total amount to be paid
def calculate_total_amount():
    # Asking the user to enter the charge for the food
    print("*************************************************")
    food_charge = float(input("*\tEnter the charge for the food: $"))
    # Calculating the tip amount
    tip_amount = calculate_tip(food_charge)
    # Calculating the sales tax amount
    sales_tax_amount = calculate_sales_tax(food_charge)
    # Calculation of the total amount
    total_amount = food_charge + tip_amount + sales_tax_amount

    # Displaying the calculated amounts
    
    print(f"*\tCharge for the food: ${food_charge:.2f},\t\t*")
    print(f"*\tTip amount (18%): ${tip_amount:.2f},\t\t*")
    print(f"*\tSales tax amount (7%): ${sales_tax_amount:.2f},\t\t*")
    print(f"*\tTotal amount: ${total_amount:.2f},\t\t\t*")
    print("*************************************************")

# Call the main function
calculate_total_amount()
