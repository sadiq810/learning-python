
# def hello_function(name):
#     print('Hello :'+name)
#
# hello_function('Ali')

# def multiply(x):
#     return x * 10
#
# print(multiply(2))
# print(multiply(4))


# => Key Value arguments
# def fruits(fruit1, fruit2, fruit3):
#     print('First Fruit: '+ fruit1)
#     print('First Second: '+ fruit2)
#     print('First Third: '+ fruit3)
#
# fruits(fruit1 = 'Apple', fruit3= "Banana", fruit2 = "Mango")

# => Arbitrary args: passing tuple to a function
# def new_function(*fruits):
#     print('The fruit is: '+fruits[2])
#
# new_function("banana", "apple", "mango")

# => Recursion function
# def new_recursion(n):
#     if(n > 0):
#         result = n + new_recursion(n-1)
#         print(result)
#     else:
#         result = 0
#
#     return result
#
# print("\n\n recursion result")
# new_recursion(9)

#=> Anonymous function or Lambda function

# a = lambda x: x + 20
# b = lambda x,y: x * y
# c = lambda x, y, z: x+y+z
#
# print(a(10))
# print(b(10, 20))
# print(c(10, 20, 30))

#lambda function usage inside another function
def new_multiplied(k):
    return lambda x: x * k

print(new_multiplied(2)(3))