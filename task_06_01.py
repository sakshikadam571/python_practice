#1
"""
name ='sakshi'
print(name )

#2
name1 = "python"
print(len(name1))

#3
name2 = "Karan"
print(name2[0])

#4
name3 = "Maharashtra"
print(name3.upper())

#5
print(name3.lower())

#6
name4 = "      Hello  python  " 
print(name4.strip())  

#7
print("rashtr" in name3)

#8
x = "Hello"
y = " World!"
print(x + y)

#9
name5 = "India"
print(name5[::1])

#10


#11
print(name1[5])


#12
print(name3[:4])


#13
print(name3[3:])


#14
print(name3[::2])


#15
print("text" is not name3)

#16
name6 = "Hello Maharashtr"
print(name6.replace("a","A"))


#17
name7= "Hello Maharastra proud to be your son"
print(name7.split())

#18
print(name2[::-1])


#19
print(name1[2:3])


#20
print(len(name4.strip()))


#21
reverse = "karan"
print(reverse[-1:-6:-1])
    
      
#22
a_count ="Maharastra"
print(a_count.count("a"))

#23
extract ="Maharastra"
print(extract[4:10])

#24
reverse1= "Maharastra"
print(reverse1[::-1])
      

#25
alternate = "programming"
print(alternate[::2])

#26
original ="Madam"
new = original[::-1]
print(original == new)

#27
string =" Hello Maharastra "
print(string.strip())

#28
string1 = "Maharastra"
print(string1[-5:1])

#29
name8 = "python is easy language"
words = name8.split()
print(words[0] +"\n"+ words[1] +"\n"+ words[2] +"\n" + words[3])


#30
age=21
print(age)

#1
value=3.1416
print(value)

#2
f_name="Sakshi"
print(name)

#3
last_name="kadam"
print(last_name)

#4
City_name="Nashik"
print(City_name)

#5
num1 = 2
num2 = 5
temp = num1 
num1 = num2
num2 = temp
print("num1:",num1)
print("'num2:",num2)


#6
x=3.5
y=12.0
print(y,x)

#8
student_count=35
average_marks=80.5
print("Student_Count:", student_count)
print("average_Marks:", average_marks)

#9
value=3.14
print("constant value:",value )
value=3.1415
print("modify value:", value)

#10
a=5
b=8
c=10
print( a )
print( b )
print( c )

#11
myAge = 21
MyAge = 20
my_age = 19
print("camel case (myAge):", myAge)
print("pascal case (MyAge):", MyAge)
print("snake case  (my_age):",my_age)

#12
pi=3.14
GRAVITY=9.8
print("sum of pl and GRAVITY:", pi + GRAVITY )

#13
number1 = 10   
_num = 5
print("number1") 
print("_num")


#14
my_var = 10
total1 = 20
print(my_var)
print(total1)

#15
total_number_of_students_in_class = 45
print(total_number_of_students_in_class)

#16
TotalNumberOfStudents = 80
total_number_of_students = TotalNumberOfStudents

print(total_number_of_students)

#17
total_number_of_students = 40
totalNumberOfStudents = total_number_of_students
print(totalNumberOfStudents)

#18
age = 15
Age = 16
AGE = 17

print(age)
print(Age)
print(AGE)

#19
SPEED_OF_LIGHT = 299792458  
distance = SPEED_OF_LIGHT * 5   
half_speed = SPEED_OF_LIGHT / 2
print("Speed of light:", SPEED_OF_LIGHT)
print("Distance in 5 seconds:", distance)
print("Half of speed of light:", half_speed)

#20
firstName = "Sakshi"
lastName = "Kadam"
age = 21
print("My name is", firstName, lastName, "and I am", age, "years old.")

#21
MAX_NUMBER_OF_USERS = 100
print("Maximum number of users allowed:", MAX_NUMBER_OF_USERS)

#22
basic_salary = 5000
bonus_amount = 1500
total_salary_amount = basic_salary + bonus_amount
print("Total salary amount:", total_salary_amount)

#23
class_name = 10
print(class_name)

#24
length = 5
breadth = 3
height =  2
volume = length * breadth * height
print("Length:", length)
print("Breadth:", breadth)
print("Height:", height)
print("Volume of the cuboid:", volume)

#25
counter1 = 0
for _ in range(5):
    counter1 += 1
print(counter1)

#26
itemPrice = 10.5
itemQuantity = 3
totalPrice = itemPrice * itemQuantity
print(totalPrice)

#27
class MyClass:
    ClassValue = 42 
print(MyClass.ClassValue)

#28
MAX_SPEED = 120
MIN_SPEED = 60
AVG_SPEED = (MAX_SPEED + MIN_SPEED) 
print("Average Speed:", AVG_SPEED)

#29
x = 10
y = 20 
z = 30
print(x)
print(y)
print(z)    

#1
# print("Hello python")


# #2
# name = "sakshi"
# age = 21
# print("name:", name)
# print("Age:",age)

# #3
# a = b= c= 20
# print("a =", a)
# print("b =",b) 
# print("c =",c)

# #4
# x ,y,z =10,20,30
# print("a =",x)
# print("b =",y)
# print("c =",z) 


#5

# string =input("Enter a string: ")
# print(len(string)) 

#6
s = input("Enter a string:")
print("first character:",s[0])
print("Last character:", s[-1])



#7
# s = input("Enter a string:")
# word = input("Enter word to search:")
# if word in s:
#     print("word exists in the string")
# else:
#     print("word does not exist in the string")
  

# #8
# s = input("Enter a string: ")
# print("Uppercase:", s.upper())
# print("Lowercase:",s.lower())

#9
# x = 11
# def show():
#     x = 20
#     print("Inside function (local x):",x)
# show()
# print("Outside function (global x):",x)

# #12
# x = 10
# def change_value():
#     global x 
#     x = 20
# change_value()
# print("After function call:")


# #13
# number = [10,20,30]
# a,b,c  =number
# print("a =",a)
# print("b =",b)
# print("c =",c)

# #14
#
# text = input("Enter a string:")
# first_five = text[:5]
# print("First 5 characters:",first_five)
# alternate_char = text[::2]
# print("Alternate character:",alternate_char)
# """

# #17
#  sentence = input("Enter a sentence:")
#  words = sentences.split() 
#  print("List of words:,")


  #18
# words = ["Hello","World","this","is","python"]
# result =  " ".join(words)
# print(result)

#19
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("a == b :", a == b)
# print("a != b :", a != b)
# print("a > b  :", a > b)
# print("a < b  :", a < b)
# print("a >= b :", a >= b)
# print("a <= b :", a <= b)

#20
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Addition (+):", a + b)
# print("Subtraction (-):", a - b)
# print("Multiplication (*):", a * b)
# print("Division (/):", a / b)
# print("Modulus (%):", a % b)
# print("Exponentiation (**):", a ** b)
# print("Floor Division (//):", a // b)

#21
# print("Boolean of integer 0:", bool(0))
# print("Boolean of integer 10:", bool(10))

# print("Boolean of float 0.0:", bool(0.0))
# print("Boolean of float 5.6:", bool(5.6))

# print("Boolean of empty string:", bool(""))
# print("Boolean of non-empty string:", bool("Python"))

# print("Boolean of empty list:", bool([]))
# print("Boolean of non-empty list:", bool([1, 2, 3]))

# print("Boolean of empty tuple:", bool(()))
# print("Boolean of non-empty tuple:", bool((4, 5)))

# print("Boolean of empty dictionary:", bool({}))
# print("Boolean of non-empty dictionary:", bool({"a": 1}))

# print("Boolean of None:", bool(None))


#22
# num = float(input("Enter a number: "))
# if num > 0:
#     print("The number is Positive")
# elif num < 0:
#     print("The number is Negative")
# else:
# print("The number is Zero")

#23
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("a > 0 and b > 0 :", a > 0 and b > 0)
# print("a > 0 or b > 0  :", a > 0 or b > 0)
# print("not (a > 0)    :", not (a > 0))

#24
# text = input("Enter a string: ")
# result = ""
# for ch in text:
#     if ch.lower() in "aeiou":
#         result += "*"
#     else:
#         result += ch
# print("Modified string:", result)

#25
# include <stdio.h>
# int main() {
#     char str[] = "Hello World";
#     int i = 0;
#     while (str[i] != '\0') {   
#         printf("%c\n", str[i]); 
#         i++;
#     }

#     return 0;
# }

#26
# s = input("Enter a string: ")
# s = s.replace(" ", "").lower()
# if s == s[::-1]:
#     print("The string is a palindrome")
# else:
#     print("The string is a palindrome")
#     print("The string is not a palindrome")

#27
# sentence = input("Enter a sentence: ")

# words = sentence.split()
# reversed_words = [word[::-1] for word in words]

# result = " ".join(reversed_words)
# print("Output:", result)


#28
# s = input("Enter a string: ")

# upper = lower = digit = special = 0

# for ch in s:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
#     elif ch.isdigit():
#         digit += 1
#     else:
#         special += 1

# print("Uppercase letters:", upper)
# print("Lowercase letters:", lower)
# print("Digits:", digit)
# print("Special characters:", special)

#30
# s = input("Enter a string:")
# first_char = s[0:1]
# last_char = s[-1:]
# result =(len(s)> 5) and (first_char == last_char)



#1
stud = [1,1,2,3,4,7,7,6]
print(stud)
print(len(stud))

#2
number = [10,20,30,40]
print(number)
print(len(number))


#3
data = [10,3.5,"python",True]
print(data)

# #4
# list = [1,2,3,4,5]
# print("First element:",list[0])
# print("Last element:", list[-1])


#5
# list = [10,20,30,40]
# print(list[-2])


#6
# list = [5,10,15,20]
# print(10 in list)


# #7
# list = [1,2,3]
# list[0] = 100
# print(list)


#8
# list = [1,2,3]
# list.append(4)
# print(list)



#9
list1 = [10,20,30,40,50]
list1.insert(2,30)
print(list1)

#10
# my_list =list((1, 2, 3, 4, 5))
tuplevar = (1,2,3,4,)
mylist = list(tuplevar)

print("The list is:", mylist)

#11
# list = [1,2,3]
# list.clear()
# print(list)


# #12
# list = [10,20,30,40,50]
# print(list[1:5])


#13
# list = [1,2,3,4,5]
# list[1:4] = [20,30,40]
# print(list)

#14
# a = [1,2,3]
# b = [4,5]
# a.extend(b)
# print(a)  


# #15
# list = [1,2]
# t = (3,4)
# list.extend(t)
# print(list)

#16
# list = [1,2]
# s = {3,4}
# list.extend(s)
# print(list)


#17
# list = [1,2]
# d = {3:"a",4:"b"}
# list.extend(d)
# print(list)

# #18
# list = [10,20,30]
# list.remove(20)
# print(list)


#19
# list = [10,20,30]
# list.pop(1)
# print(list)


#20
# list = [10,20,30]
# del list[0]
# print(list)


#21
# list = [5,2,9,1]
# list.sort(reverse=True)
# print(list)


#22
# list = [5,2,9,1]
# list.sort(reverse=True)
# print(list)

#23
# list = ["banana","apple","cherry"]
# list.sort()
# print(list)


# #24
# list = ["apple","banana","cherry","apple"]
# list.sort(key=str.lower)
# print(list)

# #25
# list = [1,2,3,4]
# list.reverse()
# print(list)


# #26
# a = [1,2,3]
# b = [a]
# b. append(4)
# print(a)
# print(b)

# #27
# a = [1,2,3]
# b = a.copy()
# b.append(4)
# print(a)
# print(b)

# #28
# a = [1,2]
# b = [3,4]
# c = a + b
# print(c)


# #29
# list = ["banana","apple","cherry","mango"]
# list.sort(key=str.lower)
# print(list)

# #30
# list = [10,20,30]
# print("Original list:",list)
# list.insert(1,15)
# print("After insert:",list)
# list.append(25)
# print("After append:",list)
# list.remove(30)
# print("After remove:",list)
# list.sort()
# print("After sorting:",list)
# list.reverse()
# print("After reversing:",list)


#1
students = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
print("List of students:", students)


#2
my_list = [10, 20, 30, 40, 50]
print("Length of the list:", len(my_list))



#3
my_list = [10, 3.14, "Python", True]
print("Elements in the list:")
for element in my_list:
    print(element)

#4
my_list = [10, 20, 30, 40, 50]
print("First element:", my_list[0])
print("Last element:", my_list[-1])


#5
my_list = [10, 20, 30, 40, 50]
print("First element:", my_list[0])
print("Last element:", my_list[-1])


#6
my_list = [10, 20, 30, 40, 50]
my_list[0] = 100
print("Updated list:", my_list)

#7
my_list = [1, 2, 3, 4]
element = 5
my_list.append(element)

print("Updated list:", my_list)


#8
my_tuple = tuple((1, 2, 3, 4))
print("Data type of my_tuple:", type(my_tuple))


#9
my_list = [10, 20, 30, 40, 50]
my_list.insert(2, 25)
print("Updated list:", my_list)

#10
my_list = [10, 20, 30, 40, 50]
my_list.clear()
print("List after clearing:", my_list)

#11
my_list = list([1, 2, 3, 4, 5])
print("List created using list() constructor:", my_list)

#12
my_list = [10, 20, 30, 40, 50, 60]
sliced_list = my_list[1:5]
print("Elements from index 1 to 4:", sliced_list)

#13
my_list = [10, 20, 30, 40, 50, 60]
my_list[1:4] = [21, 31, 41]
print("Updated list:", my_list)

#14
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("List after extending:", list1)

#15
my_list = [1, 2, 3]
my_tuple = (4, 5,6)
my_list.extend(my_tuple)
print("List after extending with tuple:", my_list)

#16
my_list = [1, 2, 3]
my_set = {4, 5, 6}
my_list.extend(my_set)
print("List after extending with set:", my_list)

#17
my_list = [1, 2, 3]
my_dict = {'a': 4, 'b': 5, 'c': 6}
my_list.extend(my_dict)
print("List after extending with dictionary:", my_list)


#18
my_list = [10, 20, 30, 40, 50]
my_list.remove(30)
print("List after removing 30:", my_list)


#19
my_list = [10, 20, 30, 40, 50]
removed_element = my_list.pop(2)
print("Removed element:", removed_element)
print("Updated list:", my_list)

#20
my_list = [10, 20, 30, 40, 50]
del my_list[3]
print("Updated list after deletion:", my_list)

#21
my_list = [50, 10, 30, 20, 40]
my_list.sort()
print("List sorted in ascending order:", my_list)


#22
my_list = [50, 10, 30, 20, 40]
my_list.sort(reverse=True)
print("List sorted in descending order:", my_list)

#23
fruits = ["banana", "apple", "cherry", "date", "mango"]
fruits.sort()
print("List sorted alphabetically:", fruits)

#24
words = ["banana", "Apple", "cherry", "Date", "mango"]
words.sort(key=str.lower)
print("List sorted alphabetically (case-insensitive):", words)

#25
my_list = [10, 20, 30, 40, 50]
my_list.reverse()
print("Reversed list:", my_list)
 
#26
list1 = [10, 20, 30]
list2 = list1
list2[0] = 100
print("list1:", list1)
print("list2:", list2)

#27
original_list = [1,2,3,4,5]
copied_list = original_list.copy()
original_list.append(6)
original_list[0] = 100
print("original List:",original_list)
print("copied List:",copied_list,copied_list)

#28
list1 = [1,2,3]
list2 = [4,5,6]
result = list1 + list2
print("first list:",list1)
print("second list:",list2)
print("joined list:",result)


#29
words = ["banana","apple","cherry","mango","grapes"]
print("Original list:",words)
words.sort(key=str.lower)
print("sorted list:",words)

#30
my_list = [10,5,20,15]
print("original list:",my_list)
my_list.insert(1,8)
print("After insert:",my_list)
my_list.append(25)
print("After append",my_list)
my_list.remove(10)
print("After remove",my_list)
my_list.sort()
print("After sort:",my_list)
my_list.reverse()
print("After reverse:",my_list)   



# 1. Write a Python program to create a set with multiple elements and print it.
num = { 1,2,3,4}
print(num)

# 2. Write a Python program to demonstrate that duplicate values are not allowed in a set.
set1 = {"sakshi",True , "Sakshi" ,False ,"Sakshi", 0.5}
print(set1)

# 3. Write a Python program to show that True and 1 are treated as the same value in a set.
set2 = {True , False ,1 ,0 }
print(set2)

# 4. Write a Python program to find the total number of elements in a set.
set3 = {"sakshi",True ," Sakshi",False ,"sakshi", 1 ,0} 
print(len(set3))
# 5. Write a Python program to create an empty set and display its type
set4 = {}
print("type of empty set:",type(set4))
# 6. Write a Python program to show that a set does not maintain insertion order.
set3 = {"sakshi",True ," Saksi",False ,"sakshi", 1 ,0} 
set3.add(2+3j)
print("not maintain insertion order of set" , set3)

# # 7. Write a Python program to prove that set elements cannot be accessed using indexing.
set6 = {"sakshi",True ," Sakshi",False ,"sakshi", 1 ,0}
try:
    print(set6[2])
except:
    print("error occured")
# TypeError: 'set' object is not subscriptable

# 8. Write a Python program to access all elements of a set using a for loop.
set2 = {"sakshi",True ," Sakshi",False ,"sakshi", 1 ,0} 
for i in set2:
    print(i)


# 9. Write a Python program to add a single element to a set using the add() method.
set3 = {"sakshi",True ," Sakshi",False ,"sakshi", 1 ,0} 
set3.add(2+3j)
set3.add( "Name" )
print("set after the adding element:" , set3)

# 10. Write a Python program to add multiple elements from a list into a set using the update()
set1 ={"Hello","Hii","By","sakshi","akshada"}
list1 = (1,2,3,4,5)
set1.update(list1)
print(set1) 
# 11. Write a Python program to remove an element from a set using the remove() method and
# handle the error if the element does not exist
my_set = {1, 2, 3}
try:
    my_set.remove(4)
except KeyError:
    print("Element not found in the set")
print(my_set)   

# 12. Remove an element using discard() when the element is not present
my_set = {1, 2, 3}
my_set.discard(4)   
print(my_set)

# 13. Remove a random element using pop()
my_set = {10, 20, 30, 40}
removed_element = my_set.pop()
print("Removed element:", removed_element)
print("Remaining set:", my_set)

# 14. Remove all elements from a set using clear()
my_set = {1, 2, 3}
my_set.clear()
print(my_set)

# 16. Join two sets using union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)

# 17. Join two sets using the | operator
set1 = {1, 2}
set2 = {3, 4}
result = set1 | set2
print(result)

# 18. Find common elements using intersection()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)

# 19. Update a set with only common elements using intersection_update()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)

# 20. Find elements present in first set but not in second using difference()
set1 = {1, 2, 3, 4}
set2 = {3, 4}
result = set1.difference(set2)
print(result)

# 21. Join a set with a list using union()
my_set = {1, 2, 3}
my_list = [3, 4, 5]
result = my_set.union(my_list)
print(result)

# 22. Demonstrate that | operator works only with sets
my_set = {1, 2}
my_list = [3, 4]
print("The | operator works only with sets")

# 23. Find difference between two sets using - operator
set1 = {1, 2, 3, 4}
set2 = {3, 4}
result = set1 - set2
print(result)

# 24. Update a set by removing elements found in another set using difference_update()
set1 = {1, 2, 3, 4}
set2 = {3, 4}
set1.difference_update(set2)
print(set1)

# 25. Find all non-common elements using symmetric_difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(result)

# 26. Find all non-common elements using the ^ operator
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 ^ set2
print(result)

# 27. Demonstrate that a set appears ordered when it contains only integers
my_set = {5, 1, 3, 2, 4}
print(my_set)

# 28. Show that mutable data types cannot be stored in a set
my_set = {1, 2}
print("Mutable data types like lists cannot be added to a set")

# 29. Join three or more sets in a single statement
set1 = {1, 2}
set2 = {3, 4}
set3 = {5, 6}
result = set1.union(set2, set3)
print(result)

my_set = {10, 20, 30}
for item in my_set:

    print(item)
