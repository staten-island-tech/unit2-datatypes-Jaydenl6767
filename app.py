# x = 3
# y = float(3)
# print(x,y)
# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(i)
# print(values[0])
# print(values[6])

# x = "this is a thing"
# y= x.split( )
# z = y[0]
# print(y)
# print(z)

# '''if day_of_week == "Friday" or "friday":
#     print("incorrect")
# else:
#     print("correct")

# x = "test"
# print(f"hello {x}")

# temp = 67
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:

# print('cold')


# def odd_even(x):
#     if x % 2 ==0:
#         print('This number is even')
#     else: 
#         print('This number is odd')
# odd_even()'''

'''def ser():
    tip = input("How was your service? Bad,Okay,Good,Great")
    s = 0
    if tip == 'Great':
        s = 0.25
    elif tip == 'Good':
        s = 0.20
    elif tip == 'Okay':
        s = 0.15
    elif tip == 'Bad':
        s = 0
    else:
        print ("Invalid")
    bill = float(input("What is your bill amount?" ))
    Subtotal = s * bill
    Total = bill + Subtotal
    print (f"This is your total {Total}")
ser()

def factor(x):
    for i in range(x):
        if (144%x==0):
            print(f"{x} is a factor")
        factor(x+1)
factor(1)'''   

def common_factor(x,y):
    GCF = 0
    for i in range(2,x):
      if x % i == 0 and y % i == 0:
            GCF = i
    print (f"{GCF} is the Greatest Common Factor")
common_factor (25,5)