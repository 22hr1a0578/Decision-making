'''
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''
def calculate_profit_loss():
    # Input for the total cost of a dozen bananas and selling price per banana
    total_cost = float(input())
    selling_price_per_banana = float(input())
    
    # Calculate the total selling price for a dozen bananas
    total_selling_price = selling_price_per_banana * 12
    
    # Determine profit or loss
    if total_selling_price > total_cost:
        profit = total_selling_price - total_cost
        print(f"Profit : Rs.{profit:.2f}")
    elif total_selling_price < total_cost:
        loss = total_cost - total_selling_price
        print(f"Loss : Rs.{loss:.2f}")
    else:
        print("No Profit No Loss")

if __name__ == "__main__":
    calculate_profit_loss()
