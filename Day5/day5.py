"""Lamda Functions"""
print("\nLamda Functions")
# Traditional function
def square(x):
    return x * x

# Lambda version
square_lambda = lambda x: x * x

print(square(4))
print(square_lambda(4))

# Add two number using lamda functions
add = lambda x, y: x + y
print(add(3, 5))

"""Decorators"""
print("\nDecorators")
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello, Hassaan!")

greet()

# Decorator with argument
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(x, y):
    print("Result:", x + y)

add(5, 3)

"""Iterators"""
print("\nIterators")
nums = [10, 20, 30]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))


"""Generators"""
print("\nGenerators")
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))

"""Comprehension"""
print("\nComprehension")
squares = [x*x for x in range(5)]
print(squares)



