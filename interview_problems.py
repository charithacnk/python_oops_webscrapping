# Acces both keys and value using items() from dictionary

details={"name":"kiran","ID":21}

for i,j in details.items():
    print(i,j)

# Python program to calculate length of string

t="Goal Is To Get A Job"

# print(len(t))

def string_length(str1):
    count=0
    for char in str1:
        count+=1#count=1+count
    return count

print(string_length(t))
 
#python function that accepts a string and calculate the number of upper case lowercase letters


def string_test(ut):
    d = {'Upper_case': 0,'lower_case': 0}
    for i in ut:
        if i.isupper():
            d['Upper_case'] +=1
        elif i.islower():
            d['lower_case'] +=1
        

    print("upper case:", d["Upper_case"])

    print("lower case letters", d['lower_case'])

string_test("Goal Is To Get A Job")

#check wether the first and last numbers are same

numbers_x=[10,20,3,4,30,11]

def first_last(numbers_x):
    first=numbers_x[0]
    second=numbers_x[-1]
    print(first,second)
    if first==second:
        return True
    else:
        return False
print(first_last(numbers_x))


#count the occurences of each word in a given sentence

def word_count(str):
    count = dict()
    words = str.split() #string coverts to list
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print( word_count('the quik brown fox jumps over the lazy dog.'))


# create a list of empty dictionaries
#[{},{},{}]


print([{} for _ in range(10)])

#extend a list without append

l1=[1,2,3,4,5]
l2=[2,4,4,5,6]
print(l1+l2)
l1.append(l2)# extend //->l1[0:]=l2
print(l1)

#python program to solve the fibonacci sequence using recursion
# n=int(input("enter the value: "))

# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return(fib(n-1)+fib(n-2))
# print(fib(n))

#find the largest number among the three input numbers

# l=[44,45,43,55]
# print(max(l))
# num1=float(input("Enter the number:"))
# num2=float(input("Enter the number:"))
# num3=float(input("Enter the number:"))

# if (num1>=num2) and (num1>=num3): #1>=2 and 1>=3
#     largest=num1

# elif (num2>=num1) and (num2>=num1):#2>=1 and
#     largest=num2
# else:
#     largest=num3
# print(f"the largest number is:{largest}")



nl= input("enter the value with space: ")

num_list= [int(n) for n in nl.split()]


largest=max(num_list)

print(f"the largest number is:{largest}")

