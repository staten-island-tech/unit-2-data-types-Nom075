""" x = 3
y = float(x)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """



""" def add(x,y,z):
    print(x+y+z)

wallet = input("How much money do you have?")
if wallet == "0":
    print("You are broke")

day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")  

add("How do you only have", wallet, "$?") """

test = "NA"




""" def factor(x):
    value = []
    
    for i in range(1, x+1): 
       if not i == "0":
            if x % i == 0:
                value.append(i)
    print(value)

number = int(input("Enter a number"))
factor(number) """




    
def find_gcf(x,y):
    small = min(x, y)
    num1 = x
    num2 = y
    for i in range(1, small + 1): 
        if x % i == 0 and y % i == 0:
            gcf = i
    return gcf, num1, num2

gcf, num1, num2 = find_gcf(100, 125)


print(f"The GCF of {num1} and {num2} is: {gcf}")