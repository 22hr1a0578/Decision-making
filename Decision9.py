'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z. A single lab needs to be allocated to a class of 'n' students. How many of the 3 labs can accommodate 'n' students?
Input format:
Input consists of 4 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the number of students(x)
Output format:
Print the number of labs which can accommodate the 'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
2 
'''
def count_accommodating_labs():
    # Input for seating capacities of the labs and the number of students
    L1_capacity = int(input())
    L2_capacity = int(input())
    L3_capacity = int(input())
    num_students = int(input())
    
    # Initialize a counter for the number of labs that can accommodate the students
    count = 0
    
    # Check each lab's capacity against the number of students
    if L1_capacity >= num_students:
        count += 1
    if L2_capacity >= num_students:
        count += 1
    if L3_capacity >= num_students:
        count += 1
    
    # Output the count of labs that can accommodate the students
    print(count)

if __name__ == "__main__":
    count_accommodating_labs()
