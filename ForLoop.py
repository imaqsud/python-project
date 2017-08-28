#code print elements of a list using for loop
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for var in list:
    print var

#code to print table of 17
multiple = 17

for var in range(1, 11):
    print var*multiple

#code to find sum of numbers from 1 to 100
sumOf=0
for var in range(1, 101):
    sumOf+=var
print sumOf

#code to print number simple pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print j,
    print

#code to print pyramid
for i in range(1, 6):
    for j in range(5, i-1, -1):
        print "*",
    print

#pass implementation
for i in range(1, 6):
    if i==1:
        pass
    elif i==2:
        print "hey, this is 2"
    else:
        print "yes"
