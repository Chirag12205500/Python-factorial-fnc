def factorial(x):
    """This is a recursive fuction
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))
num = 3
print("The factorial of",num,"is",factorial(num))

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms = 15
#check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))

def mySum(*args):
    sum1=0
    for i in args:
        sum1 = sum1+i
    return(sum1)
print(mySum(1,2,3,4,5,6,7))#7 arguments
print(mySum(1,2)) #2 arguments
print(mySum(1,2,3)) #3 arguments

def mySum(*args):
    sum1 = 0
    for i in args:
        sum1 = sum1+i
    return(sum1)
print(mySum(1,4,8,9,))


def largestNumber(*numbers):
    m=numbers[0]
    for num in numbers:
        if num > m:
            m = num
    print("largest:",m)
#write your code here
largestNumber(1,2,3,4)    #4 arguments
largestNumber(8,9,4,2,5)   #6 srguments


tax = lambda salary: salary * 20 / 100
salary = int(input("Please enter your salary:"))
print("Tax to be paid is",tax(salary))

doublenum = lambda x: x*2
a=int(input("a: "))
print(doublenum(a))
x = lambda a, b: a*b
print(x(5,6))

def squares(x):
    return x**2
list1 = [1,2,3,4,5]
#using the square func inside map function
print(list(map(squares,list1)))
print(list(map(lambda x: x**2, list1)))
print([x ** 2 for x in list1])

#filter fumnction
a = [1,2,3,5,7,9]
b = [2,3,6,7,9,8]
print(list(filter(lambda x : x in a,b)))
print([x for x in a if x in b])

def largestinthree(a,b,c):
    if a>b and a>c:
            return a
    elif b>a  and b>c:
        return b
    else:
        return c
num1=int(input("Please enter a value for num1:"))
num2=int(input("Please enter a value for num2:"))
num3=int(input("Please enter a value for num3:"))
result=largestinthree(num1,num2,num3)
print("largest of the values enetred is",result)

def computeGCD(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if((x%i==0)and(y%i==0)):
            gcd=i
    return gcd
a=int(input("x:"))
b=int(input("y:"))
print(computeGCD(a,b))


def square(x):
    x = x * x
    return x
def double(x):
    x = x * 2
    return x
num = int(input("num: "))
print("double,squaring the value:", square(double(num)))

def compose(*functions):
    def inner(arg):
        for f in reversed(functions):
            arg = f(arg)
        return arg
    return inner
#Define three function
def square (x):
    return x ** 2
def increment (x):
    return x + 1
def half (x):
    return x / 2
#call with 3 functions
composed = compose(square, increment,half) #square(increment(half(x)))
print(composed(5))
composed = compose(square,increment)
print(composed(5))
