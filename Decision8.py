'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
'''
def find_min_capacity_lab():
    # Input for seating capacities and the allocated lab
    L1_capacity = int(input())
    L2_capacity = int(input())
    L3_capacity = int(input())
    allocated_lab = input().strip()

    # Create a dictionary to store the lab capacities
    lab_capacities = {
        "L1": L1_capacity,
        "L2": L2_capacity,
        "L3": L3_capacity
    }

    # Remove the allocated lab from consideration
    if allocated_lab in lab_capacities:
        del lab_capacities[allocated_lab]

    # Find the lab with the minimal seating capacity
    min_lab = min(lab_capacities, key=lab_capacities.get)

    # Output the lab with the minimal seating capacity
    print(min_lab)

if __name__ == "__main__":
    find_min_capacity_lab()
