# <!-- You are given an interger I, find the absolute value of the integer I.



# Example 1:

# Input:
# I = -32
# Output: 32
# Explanation:
# The absolute value of -32 is 32.


# Example 2:

# Input:
# I = 45
# Output: 45
# Explanation:
# The absolute value of 45 is 45 itself.


# Your Task:
# You don't need to read input or print anything. Your task is to complete the function absolute() which takes an integer I as input parameter and return the absolute value of I.



# Expected Time Complexity: O(1)
# Expected Auxiliary Space : O(1)



# Constraints:
# -106 <= I <= 106
#  -->


#code--------------------------------------------------------#

n = int(input("enter the value: "))
asbolute = lambda x: x if x >= 0 else -x
print(asbolute(n))

#code--------------------------------------------------------#
n = int(input("enter the value: "))
def absolute(I):
    if I < 0:
        return -I
    else:
        return I    
print(absolute(n))

#code--------------------------------------------------------#