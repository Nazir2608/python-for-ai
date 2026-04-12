# operator 

def add(x, y):
    return x + y

print(add(5, 3))

# Basic math
print(10 + 3)  
print(10 - 3)  
print(10 * 3)  
print(10 / 3) 

# Special operators
print(10 // 3) 
print(10 % 3)   
print(10 ** 3)
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 5)
print(10 >= 10)
print(10 <= 5)
print(True and False)
print(True or False)
print(not True)
print(not False)
print(10 > 5 and 3 < 4)
print(10 > 5 or 3 > 4)
print(not (10 > 5))

result1 = 2 + 3 * 4      
result2 = (2 + 3) * 4  
print(result1)
print(result2)



age = 17
has_license = True
if age >= 18 and has_license:
    print("You can drive.")
else:    print("You cannot drive.")

day = "Saturday"
is_weekend=day=="Saturday" or day=="Sunday"
print("Is it the weekend?", is_weekend)

if not is_weekend:
 print("It's a weekday.")
else: print("It's the weekend.")


is_adult = age>=18
print("Is the person an adult?", is_adult)

score = 85
score=score + 5
print("Updated score:", score)
score += 5
print("Updated score with += operator:", score)
score -= 10
print("Updated score with -= operator:", score)
score *= 2
print("Updated score with *= operator:", score)
score /= 4
print("Updated score with /= operator:", score) 



first_name = "Jane"
last_name = "Doe"
full_name=first_name +" "+last_name
print("Full name:", full_name)
greeting =f"Hello, {first_name}"
print(greeting)

age = 25
message=f"I am {age} years old."
print(message)  


star = "*"
print(star * 10)
print("Hello " * 3)
separator = "-"
print(separator * 20)

text = "Python Programming"
print(text[0])
print(text[7])
print(text[-1])
print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[7:18])
print(text.lower())
print(text.upper())
print(text.replace("Python", "Java"))
print(text.split())
print(text.title())



messy = "  hello world  "
cleaned=messy.strip()
print("Cleaned text:", cleaned)

price = "$19.99"
clean_price = price.strip("$")
print("Clean price:", clean_price)  


# Check if something exists

message = "I love Python programming with Python"
print("Python" in message)
print("Java" in message)
print(message.startswith("I"))
print(message.endswith("Python"))

# Find position
print(message.find("Python"))
print(message.find("Java"))
print(message.count("Python"))  

#Replace

new_message = message.replace("Python", "Java")
print(new_message)  