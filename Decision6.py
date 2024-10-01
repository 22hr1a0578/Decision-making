'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
'''
def calculate_age():
    # Input for the last two digits of the birth year and current year
    birth_year = int(input())
    current_year = int(input())
    
    # Determine the full years based on the inputs
    # Assume the birth year is in the 1900s or 2000s based on the current year
    if current_year >= birth_year:
        age = current_year - birth_year
    else:
        # If the current year is less than the birth year, assume the birth year is in the 1900s
        age = (100 + current_year) - birth_year
    
    # Output the user's current age
    print(age)

if __name__ == "__main__":
    calculate_age()
