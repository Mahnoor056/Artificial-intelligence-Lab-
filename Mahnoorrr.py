
#Task 1
num = int(input("Enter a number "))
temp = num
revers=0
while temp>0:
    digit = temp%10
    revers= digit + revers*10
    temp= int(temp/10)
print("Reverse of",num,"is",revers)



#Task 2

sum = 0

i =0

while i<4:
    s = input("Enter a Number :")
    n = int (s)
    if n%2==0:
     sum= sum+n
    i=i+1

print("sum of Even Number is  ", sum)








#Task 3


n=int(input('how many terms to be displayed:'))
fibonacci=(0,1)
for i in range(2,n):
    fibonacci+=(fibonacci[i-2]+fibonacci[i-1],)
print(fibonacci)



#Task 4

n = int(input("Enter Your Marks between 1 to 100: "))

if (n>=91):
    print("You got Grade 'A' ")
elif n>=81 and n<91:
    print("You got Grade 'B' ")
elif n>=71 and n<81:
    print("You got Grade 'C' ")
elif n>=61 and n<71:
    print("You got Grade 'D' ")
elif n>=50 and n<61:
    print("You got Grade 'E' ")
else:
    print("Sorry! You are Fail ")

#Task 5

num = int(input("Enter a Number: "))
fac = 1
for i in range(1, num + 1):
    fac = fac * i
print("factorial of ", num, " is ", fac)