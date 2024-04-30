#!/usr/bin/python3

numbers=[11,26,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num%2==0:
        print('the list contains an even number', num)
        continue
else:
    print('the list does not contain an even number')

def mydiv(items, beneficiaries):
 assert (items>beneficiaries),"Items to be shared are less"
 return items/beneficiaries
print (mydiv(20,4))


print (mydiv(4,10)) # the program will crash at this point
print (mydiv(9,4))
print (mydiv(7,0))
print (mydiv(12,3))