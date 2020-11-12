# Python Basic (Part -I) - Exercises, Practice, Solution https://www.w3resource.com/python-exercises/python-basic-exercises.php

"""
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""
print("Twinkle, twinkle, little star,\n \t How I wonder what you are! \n \t \t Up above the world so high,  \n \t \t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n \tHow I wonder what you are")

"""
2. Write a Python program to get the Python version you are using.
"""
import sys
print("I am using Python version", sys.version)

"""
3. Write a Python program to display the current date and time.
"""
import datetime
print("Current date and time is ", datetime.datetime.now())

"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
"""
# import math
# def calculate_circle_area(radius):
#     return math.pi * (radius * radius)
#
# inputRadius  = float(input("Enter the radius: "))
# print("Area of the circle is", calculate_circle_area(inputRadius))

"""
5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""
# firstname = input("Enter you first name: ")
# lastname = input("Enter your last name: ")
# print(f"Output {lastname} {firstname}")

"""
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
# input_number = input("Sample Data: ")
# _list = input_number.split(",")
# _tuple = tuple(_list)
# print(f"List {_list}")
# print(f"Tuple {_tuple}")

"""
 7. Write a Python program to accept a filename from the user and print the extension of that.
"""
# def extract_file_extension(filename):
#     return filename.split(".")[-1]
# input_filename = str(input("Enter file name: "))
# print("Your file extension is ", extract_file_extension(input_filename))

"""
8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
"""
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
exam_st_date = (11, 12, 2014)
print(" The examination will start from : %i / %i / %i"%exam_st_date)

"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615

(The problem is ambiguous. I thought nn = n*n and nnn means n*n*n.)
"""
# My first attempt
# n = int(input("Sample value of n is : "))
# print("Expected Result : ", n + pow(n, 2) + pow(n,3))

# My second attempt
n = int(input("Sample value of n is : "))
n1 = int("%s" % n)
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))
print("Expected Result : ", n1 + n2 + n3)


