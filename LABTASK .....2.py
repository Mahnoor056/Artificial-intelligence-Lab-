#ACTIVITY 1

mylist1=[]
print("enter objects of first list...")
for i in range(5):
    val=input ("enter a value:")
    n=int(val)
    mylist1.append(n)
mylist2=[]
print("enter objects of seconf list...")
for i in range(5):
    val=input ("enter a value:")
    n=int(val)
    mylist2.append(n)
list3=mylist1+mylist2
print(list3)


#ACTIVITY 2

def isPalindrome(word):
    temp=word[::-1]
    if temp.capitalize()==word.capitalize():
        return True
    else:
        return False
print(isPalindrome("deed"))



#ACTIVITY 3

a=[[1,0,0],[0,1,0],[0,0,1]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[]
for indrow in range(3):
    c.append([])
    for indcol in range(3):
        c[indrow].append(0)
        for indaux in range(3):
            c[indrow][indcol]+=a[indrow][indcol]*b[indrow][indcol]
print(c)

#ACTIVITY 4

def perimeter(listing):
    leng=len(listing)
    perimeter=0;
    for i in range(0,leng-1):
        dist=(((listing[i][0]-listing[i+1][0])**2)+
              ((listing[i][1]-listing[i+1][1])**2))**0.5
        perimeter=perimeter+dist
    perimeter=perimeter+(((listing[0][0]-listing[leng-1][0])**2)
                         +((listing[0][1]-listing[leng-1][1])**2))**0.5
    return perimeter
L=[(1,3),(2,7),(3,9),(-1,8)]
print(perimeter(L))
               
        
#ACTIVITY 5
def symmDiff(a,b):
    e=set()
    for i in a:
        if i not in b:
            e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e
set1={0,1,2,4,5}
set2={4,5,7,8,9}
print(symmDiff(set1,set2))
print(set1.symmetric_difference(set2))

print(set2.symmetric_difference(set1))

print(set1^set2)
print(set2^set1)

#ACTIVITY 6
sample={("shoaib","ali"):"0246585468445",("aib","li"):"3431233563",("sib","al"):"012344322433",}
firstName=input("enter first name")
lastName=input("enter last name")
searchTuple=(firstName,lastName)
if searchTuple in sample:
    print(sample[searchTuple])
else:

    print("name not found")
    

#TASK 1
list1=[]
list2=[]
print("enter 6 elements for first list:")
for i in range(6):
    list1.append(input())
print("\nenter 6 elements for second list:")
for i in range(6):
    list2.append(input())
list3=[]
for i in range(6):
    
    list3.append(list1[i])
for i in range(6):
    
    list3.append(list2[i])
print("\nthe new (merged) list is:")
print(list3)

#task 1 2
list1=[]
list2=[]
print("enter 6 elements for first list:")
for i in range(6):
    list1.append(input())
print("\nenter 6 elements for second list:")
for i in range(6):
    list2.append(input())
list3=[]
for i in range(6):
    
    list3.append(list1[i])
for i in range(6):
    
    list3.append(list2[i])
print("\nthe new (merged) list is:")
print(list3)

print("max:",max(list3),"\nmini",min(list3))
    
# task 3
from math import *
x=float(input("enter x"))
h=float(input("enter h"))
m=(sin(x+h)-sin(x))/h
n=cos(x)
print(m)
if(m==n):
     print("equal")   
else:
    print("not equal")

#task 4
birthdays={'Albert einstein':'03/14/1879',
          'benjamin franklin':'01/17/1706',
          'ada lovelace':'06/14/1593'}
print('welcome to the birthday dictionary. we know the birthday of:')
for name in birthdays:
    print(name)
print('who\'s birthday do you want to look up?')
name=input()
if name in birthdays:
    print('{}\'s birthday is {}.'.format(name,birthdays[name]))
else:
    print('sadly, we don\'t have{}\'s birthday.'.format(name))

    
# task 5
sample_dict={
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"newyork"}
keys=["name","salary"]
newDict={k:sample_dict[k] for k in keys}
print(newDict)


