
#1. will the code run, and if so, what will be the data types and values of a and b?
a, b = [10, 11] #a, b will be integer
a, b = [10] #won't run
a, b = [10, 11, 12] #won't run
a, *b = [10, 11] #a will be integer and b will be list with only one element
a, *b = [10] #a will be integer and b will be list with no element
a, *b = [10, 11, 12] #a will be integer and b will be list with two elements


#2. what data type is args and kwargs inside the function, what are the values,
#and how would you use them?
def base_function(*args, **kwargs):
    return args, kwargs

base_function()
base_function(['A', 'B']) #all will be in *args as list
base_function('Hello', 'World', '!') #all will be in *args as list
base_function(answer=True, question='No') #all will be in *kwargs as dictionary
base_function('a', 'b', c='value', d=10) #'a' and 'b' will be in *args and c='value' & d=10 will be in *kwargs


#3. write a lambda function that is passed into my_func, and performs a valid
#operation on a and b, without editing the contents of my_func at all.

def my_func(a, b, func=lambda a, b: sum([a,b])):
    value = func(a, b)
    return value

