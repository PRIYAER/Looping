#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.
Sample Input :
48
Sample Output :
64
"""

n=int(input())
powerof2=1
while powerof2<=n:
    powerof2 *= 2
print(powerof2)


# In[2]:


"""Write a code get an integer number as input and print the sum of the digits.
Sample Input :
124
Sample Output :
7
"""

n=int(input())
r=0
while n!=0:
   d=n%10
   r=d+r
   n=n//10
print(r)
    


# In[3]:


"""Write a code to get an integer N and print values from 1 till N in a separate line.
Sample Input :
5
Sample Output :
1
2
3
4
5
"""

n=int(input())
for i in range(1,n+1):
    print(i)


# In[4]:


"""Write a code to get the input and print it 5 times.
Sample Input :
4
Sample Output :
4
4
4
4
4
"""

n=int(input())
for i in range(5):
    print(n)


# In[5]:


"""Write a program to get a string as input and reverse the string without using temporary variable.
Sample Input :
GUVI
Sample Output :
IVUG
"""

s=input()
a=s[::-1]
print(a)


# In[6]:


"""Write a code to get 2 integers A and N. Print the integer A, N times in separate line.
Sample Input :
2 3
Sample Output :
2
2
2
"""

a,b=list(map(int,input().split()))
for i in range(b):
    print(a)


# In[7]:


"""Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.
Sample Input :
2 3
Sample Output :
1
"""

a,b=list(map(int,input().split()))
mini=min(a,b)
hcf=0
for i in range(1,mini+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)


# In[8]:


"""Write a code to get 2 integers as input and add the integers without any carry.
Sample Input :
44 66
Sample Output :
0
"""

def add_without_carry(num1, num2):
    # Convert numbers to strings to iterate over each digit
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Pad the shorter number with leading zeros
    max_len = max(len(str_num1), len(str_num2))
    str_num1 = str_num1.zfill(max_len)
    str_num2 = str_num2.zfill(max_len)
    
    result = []
    
    # Add each digit without carry
    for digit1, digit2 in zip(str_num1, str_num2):
        sum_digit = (int(digit1) + int(digit2)) % 10
        result.append(str(sum_digit))
    
    # Join the result list into a string and convert to integer
    return int(''.join(result))

# Example usage
num1,num2 = list(map(int,input().split()))
print(add_without_carry(num1, num2))



# In[9]:


"""Write a code to get an integer N and print the even values from 1 till N in a separate line.
Sample Input :
6
Sample Output :
2
4
6
"""

n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i)


# In[11]:


"""Write a program to get a list of integers as input and find the LCM of the values without using GCD
Sample Input :
1 2 3 4 5
Sample Output :
60
"""


arr=list(map(int,input().split()))
def lcm(a,b):
    if a>b:
        greater=a 
    else:
        greater=b 
    while True:
        if greater%a==0 and greater%b==0:
            lcmresult=greater
            break
        greater+=1
    return lcmresult 
    
def findlcm(arr):
    result = arr[0]
    for i in arr:
        result=lcm(result,i)
    return result
print(findlcm(arr))


# In[12]:


"""Write a code to get an integer N and print the sum of  values from 1 to N.
Sample Input :
10
Sample Output :
55
"""

n= int (input())
s=0
for i in range(n+1):
    s=s+i
print(s)


# In[13]:


"""Write a code get an integer number as input and print the odd and even digits of the number separately.
Sample Input :
1234
Sample Output :
2 4
1 3
"""

a=input()
b=[]
for i in a:
    b.append(int(i))
even=[]
odd=[]
for i in b:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(*sorted(even))
print(*sorted(odd))


# In[14]:


"""Write a code to get an integer N and print the digits of the integer.
Sample Input :
348
Sample Output :
3 4 8
"""

n=list(input())
for i in range(1):
    print(*n,sep=' ')


# In[15]:


"""Write a code to get an integer N and print the values from N to 1.
Sample Input :
10
Sample Output :
10
9
8
7
6
5
4
3
2
1
"""

n=int(input())
for i in range(n,0,-1):
    print(i)


# In[ ]:




