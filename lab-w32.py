#fix the problems with each of these classes (1-3)

#1
class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#2
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        self.x = a + b
my_instance = MyClass()
my_instance.x

#3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#4 A Fibonacci sequence is a list of values where each is the sum of the previous
#  two, e.g. [0, 1, 1, 2, 3].
#      - First write a function that takes in a list of any two values, then
#        calculates the rest of the sequence starting from that point.  It
#        should have two arguments; the starting list, and the number to
#        calculate.
#      - Second, turn this into a class that takes the same list at start,
#        but has a method that takes N as an argument and then calculates
#        the sequence.
#  Note that technically the Fibonacci sequence starts at 0, but for our
#  coding practice we can calculate it from any two starting values.

def fibonacci(start_list, num_to_cal):
    final_list = [i for i in range(num_to_cal)]
    for i in range(num_to_cal):
        if i < 2:
            final_list[i] = start_list[i]
        elif i >= 2:
            final_list[i] = final_list[i-2] + final_list[i-1]
        
    return final_list
            
fibonacci([2, 3], 7)

class MyFib():
    def __init__(self, input_list):
        self.num = input_list
    def fib_cal(self, N):
        for N in range(N):
            if N >= 2:
                self.num.append(self.num[N-2] + self.num[N-1])
        return self.num

my_instance = MyFib([2, 3])
my_instance.fib_cal(10)

#Solution
def fibonacci(vals, n):
    for _ in range(n):
        new_val = sum(vals[-2:])
        vals.append(new_val)
    return vals

class MathOnLists():
    def __init__(self, vals):
        self.vals = vals
    
    def fibonacci(self, n):
        fib_vals = self.vals
        for _ in range(n):
            new_val = sum(fib_vals[-2:])
            fib_vals.append(new_val)
        return fib_vals

math_instance = MathOnLists([0,1])
math_instance.fibonacci(10)
