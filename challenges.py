import functools
# Fizzbuzz
'''
Write a short program that prints each number from 1 to 100 on a new line.

For each multiple of 3, print "Fizz" instead of the number.

For each multiple of 5, print "Buzz" instead of the number.

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''

def fizzbuzz(up_to):
    for i in range(1, up_to+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "FizzBuzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        elif i % 5 == 0:
            print(i, "Buzz")

def fizzbuzz_list(up_to):
    l = []
    for i in range(1, up_to+1):
        if i % 3 == 0 and i % 5 == 0:
            l.append("FizzBuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("Buzz")
        else:
            l.append(i)
    return l


# Fibonacci
# 0 1 2 3 4 5 6 7  8
# 0 1 1 2 3 5 8 13 21
# Fn = Fn-1 + Fn-2

def fibo_iter(fibo_number):
    if fibo_number == 0:
        return 0
    elif fibo_number == 1:
        return 1
    elif fibo_number > 1:
        vp = 0
        vc = 1
        for i in range(fibo_number-1):
            fibo_val = vp + vc
            vp = vc
            vc = fibo_val
        return fibo_val

# print(fibo_iter(6))

def fibo_iter2(fibo_number):
    n = 0
    fibo_val = 0
    while n <= fibo_number:
        if n == 0:
            fibo_val = 0
            print(fibo_val)
            vp = 0
            n += 1
        elif n == 1:
            fibo_val = 1
            print(fibo_val)
            vc = 1
            n += 1
        else:
            fibo_val = vp + vc
            print(fibo_val)
            vp = vc
            vc = fibo_val
            n += 1
    return fibo_val

print(fibo_iter2(20))


def fibo_rec(fibo_num): ## Very inefficient, needs cache
    if fibo_num == 0:
        return 0
    elif fibo_num == 1:
        return 1
    fibo_val = fibo_rec(fibo_num-2)+fibo_rec(fibo_num-1)
    return fibo_val

print("fibo rec", fibo_rec(20))

# Factorial
# n! = n * (n-1)!
# 5!
# 5x4x3x2x1
[1,2,3,4,5]


def factorial_iter(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact*i
        return fact

print("factorial_iter",  factorial_iter(7))


def factorial_rec(n):
    if n == 0:
        return 1
    return n*factorial_rec(n-1)


print("factorial_rec: ", factorial_rec(1))

def factorial_red(n):
    return functools.reduce(lambda x, y: x*y, range(1, n+1))
print("factorial_red", factorial_red(7))

# Sumatorial

def summ_red(n):
    return functools.reduce(lambda x, y: x+y, range(1, n+1))
print("summ_red", summ_red(7))


# Palindrome
def is_palindrome(a_string):
    fixed_string = a_string.replace(" ", "").lower()
    return fixed_string == fixed_string[::-1]

print("is palindrome: ", is_palindrome("Anita lava la tina"))

# Remove repeated
def remove_dups(a_list):
    no_dup_list = []
    for i in a_list:
        if i not in no_dup_list:
            no_dup_list.append(i)
    return no_dup_list

# Order a list of number
my_list = [3, 5, 7, 8, 1, 2, 3]

# Find largest
def find_largest(a_list):
    i = 0
    while i <= len(a_list)-1:
        print(i)
        if i == 0:
            largest = a_list[0]
            i += 1
            continue
        if a_list[i] > largest:
            largest = a_list[i]
        i += 1
    return largest

def find_largest_2(a_list):
    largest = 0
    for i in a_list:
        if i > largest:
            largest = i
    return largest

# Reverse a string

def reverse(a_string):
    r_string = ""
    s_len = len(a_string)-1
    while s_len >= 0:
        r_string += a_string[s_len]
        s_len -= 1
    return r_string

print("reversed", reverse("Helloooo"))