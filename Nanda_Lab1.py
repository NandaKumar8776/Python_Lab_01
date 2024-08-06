# Python Lab 1
# REQUIREMENT-1: Identify if palindrome from given nested list.

print("Requirement #1")
# Code that reverses the array to compare and check.
def IsPalindrome(a):
    return a[::-1] == a


# Given list to perform the check.
given_lists = [ [1, 2, 3, 5, 7, 7, 0],
    ["Red", "Green", "Blue"],
    [1, 0, 0, 1, 0, 0, 1],
    ["Red", "Yellow", "Green", "Yellow", "Red"]]

# Using for loop to iterate between the sub-lists to perform palindrome check and print results.
for a in given_lists:
    print(f"{a} {IsPalindrome(a)}")


# REQUIREMENT-2: Element by element matrix multiplication.
print("\nRequirement #2")

# Function defenition for the multiplication.
def mul(mat_1, mat_2):
    result_matrix = [[],[],[]]
    
    # Utilising two for loops to iterate between each elements of the matrixes to perform element multiplication.
    mat1_len = len(mat_1)
    mat2_len = len(mat_1[0]) 
    
    for i in range(mat1_len):
        for j in range(mat2_len):
            result_matrix[i].append(mat_1[i][j] * mat_2[i][j])
    return (result_matrix)

# Printing the result.
print(mul([[1, 2, 3, 5, 7, -7, 0], [112, 43, 17, 6, 2, 118, 11],[1024, 512, 256, 128, 64, 32, 16]], [[9, 81, 75, 42, 5, -113, -1], [11, 2, -3, 0, 7, 0, 9], [8, 6, 2, 1, 0, -1, -2]]))


# To produce a single scalar number.
print("\nRequirement #3")

# Function defenition.
def ToMultiply(list1):
    # Creating a variable with 1 and not 0 so the multiplication does not end up as zero.
    resultScalar = 1
    for a in list1:
        resultScalar *= a
    return resultScalar

# Printing result.
print(ToMultiply([1024, 512, 256, 128, 64, 32, 16]))
