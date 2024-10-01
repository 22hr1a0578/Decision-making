'''
 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''
def allocate_lab():
    # Input for seating capacities of the labs and the number of students
    L1_capacity = int(input())
    L2_capacity = int(input())
    L3_capacity = int(input())
    num_students = int(input())
    
    # Initialize a variable to track the suitable lab
    suitable_lab = None
    
    # Check each lab's capacity and determine the best fit
    if L1_capacity >= num_students:
        suitable_lab = "L1"
    if L2_capacity >= num_students:
        if suitable_lab is None or L2_capacity > L1_capacity:
            suitable_lab = "L2"
    if L3_capacity >= num_students:
        if suitable_lab is None or L3_capacity > (L1_capacity if suitable_lab == "L1" else L2_capacity):
            suitable_lab = "L3"
    
    # Output the suitable lab
    if suitable_lab:
        print(suitable_lab)
    else:
        print("No suitable lab available")

if __name__ == "__main__":
    allocate_lab()
