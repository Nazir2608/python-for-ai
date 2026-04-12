#This is a simple Python program that demonstrates variable assignment, string concatenation, and basic arithmetic operations. 
"""
The program starts by assigning the string "Alice" to the variable 'name' and the integer 30 to the variable 'age'.
Then, it reassigns the variable 'name' to "Bob". The program prints the value of 'name' and 'age', which will output "Bob" and 30, respectively.
Next, it demonstrates string concatenation by combining 'first_name' and 'last_name' to create 'full_name', which is then printed as "John Doe".
Finally, the program performs basic arithmetic operations (addition, subtraction, multiplication, and division) on the variables 'x', 'y', 'a', and 'b', and prints the results of these operations in a formatted manner.
"""
name="Alice"
age=30
name="Bob"
print(name)
print(age)  
first_name="John"
last_name="Doe"
full_name=first_name+" "+last_name
print(full_name)
x=10
y=5
sum=x+y
print("The sum of", x, "and", y, "is", sum)
a=15
b=4
difference=a-b
product=a*b
quotient=a/b
print("The difference of", a, "and", b, "is", difference)
print("The product of", a, "and", b, "is", product)
print("The quotient of", a, "and", b, "is", quotient)