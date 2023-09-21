#TOPIC: Python Basics Variable

#Declare two variables, `x` and `y`, and assign them integer values. Swap the
#values of these variables without using any temporary variable.
v1 = 10
v2 = 20
print(f'v1 and v2 before swap {v1}, {v2}')
v1, v2 = v2, v1  #Swaping the variables
print(f'v1 and v2 after swap {v1}, {v2}')

#Create a program that calculates the area of a rectangle. Take the length and
#width as inputs from the user and store them in variables. Calculate and
#display the area.

def area_of_rectangle(length, width):      
 area = float(length) * float(width)     
 return area           

# store input
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

# display result
print(f'Area of rectangle = {length * width}')
print('Area of rectangle = ' + str(area_of_rectangle(length, width)))

print('srk'.upper())
#Write a Python program that converts temperatures from Celsius to
#Fahrenheit. Take the temperature in Celsius as input, store it in a variable,
#convert it to Fahrenheit, and display the result.

def convert(temp,unit):
 if unit.upper() == 'F':
  return(f'Temperature in Celsius : { (temp * 1.8) + 32}')  
 else:
  return(f'Temperature in Fahrenheit : {(temp-32)/1.8}')
 
temp = float(input('Enter the temperatiure : '))
unit = str(input('Enter the Unit as F or C: '))
valid_units = ['F','C']

if type(temp) != float or unit not in valid_units:
 print('Either Temperature or Unit is not in correct format..!')
else:
 print(convert(temp,unit))


#TOPIC: String Based Questions

#1. Write a Python program that takes a string as input and prints the length of the string.
str1 = str(input('Enter the String you wish: '))
print(f'given String is {str1} and the length is {len(str1)}')

#2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.
strwithVowels = str(input('Enter the String you wish: '))
vows = ['a','e','i','o','u']
count=0
for char in strwithVowels:
    if char in vows:
        count += 1
print(f'Count of Vowels in the given String is : {count}')

#3.Given a string, reverse the order of characters using string slicing and print the reversed string.
yourstr = str(input('Enter your String : '))
#slice the string in reverse order
revStr = yourstr[::-1]
print(revStr)

#4. Write a program that takes a string as input and checks if it is a palindrome
#(reads the same forwards and backwards).
yourstr1 = str(input('Enter your String : '))
if yourstr1 == yourstr1[::-1]:
    print('Given String is a Palindrome..!')
else:
    print('Given String is NOT a Palindrome..!')

#5. Create a program that takes a string as input and removes all the spaces from
#   it. Print the modified string without spaces.
yourstr2 = str(input('Enter your String : '))
print(f'string with no spaces is : {yourstr2.replace(" ","")}')



