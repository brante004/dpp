#1: this code does not run!  try it and examine the errors, then figure out what needs to
#be changed to make it work

#original problem
a = 10
def first_func(b=20):
    c = 30
    value = second_func()
    return value
def second_func(d=40):
    e = 50
    return a + b + c + d + e

result = first_func()

#my way of doing it
a = 10

def first_func(b=20):
    c = 30
    def second_func(d=40):
        e=50
        return a + b + c + d +e
    value = second_func()
    return value
#nested functions are not favorable

result = first_func()
print(result)

#below is the solution. the best way to do it is to pass the value
a = 10
def first_func(b=20):
    c = 30
    value = second_func(b, c)
    return value
def second_func(b, c, d=40):
    e = 50
    return a + b + c + d + e

result = first_func()
print(result)

#2: take this code from Thursday's lab and write a function so that the form of
#the final answer is:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}

def key_func(k):
    new_k = k.capitalize()
    return new_k

def val_func(v):
    new_v = datetime.datetime.strptime(v, "%m/%d/%Y").date()
    return new_v

answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

print(answer)

#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}
