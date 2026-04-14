#Lists

# Empty list
my_list=[]

#list with items
fruits=["apple","banana","cherry"]
numbers=[1,2,3,4,5]
mixed_list=[1,"hello",3.14,True]

print(fruits)
print(fruits[2])
print(fruits[0])   
print(fruits[1])    
print(fruits[-1])   
print(fruits[-2])   
"""Slices allow you to access a range of items in a list. The syntax is list[start:end], where start is the index of the first item and end is the index of the item just after the last item you want to include."""
print(fruits[0:2])
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])   



fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits)
fruits.insert(1, "kiwi")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.pop()
print(fruits)

del fruits[0]              # Remove by index
print(fruits)



numbers = [3, 1, 4, 1, 5, 9]

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(len(numbers))


#Checking lists
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)  
print("mango" in fruits)  

if "banana" in fruits:
    print("Banana is in the list.")

if fruits:
    print("The list is not empty.")
else:    print("The list is empty.")