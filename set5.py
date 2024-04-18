# 1. Create a list containing several strings. Take input from the user (search string); display whether
# entered string is available in the list or not.

# l = ['abc', 'have', 'a', 'geeky', 'day']
# s = str(input('Enter Search String :'))
# if s in l:
# 	print(f'{s} is present in the list')
# else:
# 	print(f'{s} is not present in the list')

# 2.Accept the string from the user; display the message whether the entered string is palindrome
# or not.

# user_str=str(input("Enter a String:"))  
# if(user_str==user_str[::-1]):  
#       print("The letter is a palindrome")  
# else:  
#       print("The letter is not a palindrome") 

# 3. Accept the string from the user; display the string in the reverse order.

# user_str=str(input("Enter a letter:")) [::-1]  
# print(user_str)

# 4. Accept the string from the user; allow user to choose from the following options and perform
# the task as per user’s choice. i). Convert to the upper case, ii). Convert to the lower case, iii).
# Convert to the swap case, iv). Convert to the title case

# user_str=str(input("Enter a String:"))
# uprcase=user_str.upper()
# print("String is Uper case:",uprcase) 
# lwrcase=user_str.lower()
# print("String is lower case:",lwrcase)
# swpcase=user_str.swapcase()
# print("String is swap case:",swpcase) 

# import cv2
# import vlc
# import time


# mp=vlc.MediaPlayer("1.mp4")

# mp.play()

# time.sleep(5)
# Task 5: Arrange strings in alphabetical order

# # Accepting multiple strings from the user
# strings_list = []
# num_strings = int(input("Enter the number of strings: "))
# for i in range(num_strings):
#     strings_list.append(input(f"Enter string {i+1}: "))

# # Sorting the list alphabetically
# strings_list.sort()

# # Displaying the sorted list
# print("Sorted strings:")
# for string in strings_list:
#     print(string)




# Task 6: Create a tuple and insert 25 at the third position

# # Creating a tuple
# my_tuple = (10, 20, 30, 40, 50)

# # Inserting 25 at the third position
# my_tuple = my_tuple[:2] + (25,) + my_tuple[2:]

# # Displaying the modified tuple
# print("Modified tuple:", my_tuple)


# Task 7: Dictionary operations

# Creating the library dictionary
library = {
    "Bookid": "B001",
    "Title": "Introduction to Python",
    "Author": "John Doe",
    "Price": 29.99,
    "Publisher": "XYZ Publications"
}

# a. Display the dictionary
print("Library dictionary:")
print(library)

# b. Display the name of Author
print("Author:", library["Author"])

# c. Display the Bookid
print("Bookid:", library["Bookid"])

# d. Display the length of the dictionary
print("Length of the dictionary:", len(library))

# e. Update the price
new_price = float(input("Enter the new price: "))
library["Price"] = new_price

# f. Insert year as the new key
year = int(input("Enter the year: "))
library["Year"] = year

# Displaying the updated dictionary
print("Updated library dictionary:")
print(library)


# Task 8: Numeric array operations

import numpy as np

# Creating a numeric array
numeric_array = np.array([1, 2, 3, 4, 5])

# Add 2 to each element
numeric_array_plus_2 = numeric_array + 2

# Subtract 3 from each element
numeric_array_minus_3 = numeric_array - 3

# Multiply each element by 3
numeric_array_times_3 = numeric_array * 3

# Divide each element by 2
numeric_array_divide_2 = numeric_array / 2

# Find max and min
max_value = np.max(numeric_array)
min_value = np.min(numeric_array)

# Find the average of all elements
average_value = np.mean(numeric_array)

# Displaying the results
print("Array plus 2:", numeric_array_plus_2)
print("Array minus 3:", numeric_array_minus_3)
print("Array times 3:", numeric_array_times_3)
print("Array divided by 2:", numeric_array_divide_2)
print("Max value:", max_value)
print("Min value:", min_value)
print("Average value:", average_value)



# Task 9: Numeric array operations

# Creating a numeric array
numeric_array = [1, 2, 3, 4, 5]

# Append an element
numeric_array.append(6)

# Pop an element
popped_element = numeric_array.pop()

# Insert an element at a desired position
position = int(input("Enter the position to insert: "))
element = int(input("Enter the element to insert: "))
numeric_array.insert(position, element)

# Reverse the elements
numeric_array.reverse()

# Convert the array to list
numeric_list = list(numeric_array)

# Displaying the results
print("Array after append:", numeric_array)
print("Popped element:", popped_element)
print("Array after insertion:", numeric_array)
print("Array after reversal:", numeric_array)
print("List conversion:", numeric_list)


# Task 10: Accept numeric elements and search for a specific element

# Accepting numeric elements from the user
numeric_array = []
num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
    element = float(input(f"Enter element {i+1}: "))
    numeric_array.append(element)

# Displaying the numeric array
print("Numeric array:", numeric_array)

# Asking user to enter search element
search_element = float(input("Enter the search element: "))

# Displaying the position of the searched element
if search_element in numeric_array:
    print("Position of the search element:", numeric_array.index(search_element))
else:
    print("Search element not found in the array.")




# Task 11: Compare corresponding elements of two arrays and display the bigger number

# Taking input for the first array
array1 = [int(input(f"Enter digit {i+1} for array 1: ")) for i in range(5)]

# Taking input for the second array
array2 = [int(input(f"Enter digit {i+1} for array 2: ")) for i in range(5)]

# Comparing corresponding elements and displaying the bigger number
for num1, num2 in zip(array1, array2):
    print("Bigger number:", max(num1, num2))



# Task 12: Accept dimension and values for an array from the user and create the array

# Accepting dimensions of the array from the user
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Accepting values for the array from the user
array_values = []
for i in range(rows):
    row_values = []
    for j in range(columns):
        value = int(input(f"Enter value for row {i+1} column {j+1}: "))
        row_values.append(value)
    array_values.append(row_values)

# Creating the array
array = np.array(array_values)

# Displaying the array
print("Array:")
print(array)



# Task 13: Function to calculate simple interest

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    Args:
    - principal (float): The principal amount.
    - rate (float): The interest rate (in percentage).
    - time (float): The time period (in years).
    
    Returns:
    - float: The simple interest.
    """
    return (principal * rate * time) / 100

# Example usage
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

simple_interest = calculate_simple_interest(principal_amount, interest_rate, time_period)
print("Simple interest:", simple_interest)



# Task 14: Function to perform basic arithmetic operations on a number

def arithmetic_operations(number):
    """
    Perform basic arithmetic operations on a number.
    
    Args:
    - number (float): The number to perform operations on.
    
    Returns:
    - dict: Dictionary containing results of arithmetic operations.
    """
    results = {
        "Square": number ** 2,
        "Cube": number ** 3,
        "Square root": number ** 0.5
    }
    return results

# Example usage
input_number = float(input("Enter a number: "))
results_dict = arithmetic_operations(input_number)
print("Arithmetic operations results:")
for operation, result in results_dict.items():
    print(f"{operation}: {result}")


# Task 15: Function to accept multiple strings and store them in a list

def store_strings(num_strings):
    """
    Accept multiple strings and store them in a list.
    
    Args:
    - num_strings (int): The number of strings to accept.
    
    Returns:
    - list: List containing the entered strings.
    """
    strings_list = []
    for i in range(num_strings):
        string = input(f"Enter string {i+1}: ")
        strings_list.append(string)
    return strings_list

# Example usage
num_input_strings = int(input("Enter the number of strings: "))
input_strings_list = store_strings(num_input_strings)
print("Strings list:", input_strings_list)



# Task 16: Find the biggest number from three values using lambda

biggest_number = lambda x, y, z: max(x, y, z)

# Example usage
value1 = float(input("Enter first value: "))
value2 = float(input("Enter second value: "))
value3 = float(input("Enter third value: "))

print("Biggest number:", biggest_number(value1, value2, value3))


# Task 17: Demonstrate the use of break and pass

# Example using break
for i in range(5):
    if i == 3:
        print("Breaking loop at", i)
        break
    print(i)

# Example using pass
for i in range(5):
    if i == 3:
        print("Skipping iteration at", i)
        pass
    else:
        print(i)
