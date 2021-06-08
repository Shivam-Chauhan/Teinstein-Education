# Brute Force
number=input("Enter a number:-")
sum1=0
for j in number:
    sum1+=int(j)*int(j)*int(j)
print(True if sum1==int(number) else False)


# We can save some computational power by breaking if sum1>number
number=input("Enter a number:-")
temp=int(number)
sum1,counter=0,0
for j in number:
    sum1+=int(j)*int(j)*int(j)
    if sum1>temp:
        print(False)
        counter=1
if counter==0 and sum1==temp:
    print(True)
elif counter==0 and sum1!=temp:
    print(False)

