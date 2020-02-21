# Date : 7-05-2018
 
# Write a program to find solution for  
# Tower of Hanoi Problem

"""
This code uses the recursion to find the solution for tower of Hanoi Problem.
"""

# Handle the user input 
try:
    # No. of disks (a positive integer
    # value greater than zero) 
    disk = int(input(""))
    
    # Error handling for negative values
    # and zero.
    if disk <= 0:
        raise Exception()
    
    # calculating minimum number of
    # moves required to solve the
    # problem with n disks.
    minimum_moves = 2**disk - 1
    # mathematical formula to calculate
    # minimum number of moves with n
    # disks is : (2^n - 1)
    
    print("The minimum number of moves required to solve the problem with", disk, "disks are : ", minimum_moves, "\n")
    
    print("------------------------------------", "\n")
    
    # a list of positive integers
    # counting number of moves.
    count = []
    
    # a function to add number of moves
    # to the list.
    def count_moves(counts):
        while counts in count:
            counts += 1
        count.append(counts)
        return str(counts)
        
        
    # Printing the solution
    def prnt_move(fr, to):
        print(count_moves(1)+".", "Move disk from", fr, "to", to)

    
    # Main function to calculate the
    # solution
    def disks(n, fr, to, spare):
        """
        n: positive integer value
           greater than zero.
        """
        # base case
        if n == 1:
            return prnt_move(fr, to)
         
        # recursive case     
        else:      
            disks(n-1, fr, spare, to)
            disks(1, fr, to, spare)
            disks(n-1, spare, to, fr)
        
        
    pole_1 = "Pole 1"
    pole_2 = "Pole 2"
    pole_3 = "Pole 3"  
    
    # calling function
    disks(disk, pole_1, pole_3, pole_2)
    
# Error handling when user gives a wrong
# input    
except:
    print("Invalid Input. You can enter only positive integers greater than zero.")

