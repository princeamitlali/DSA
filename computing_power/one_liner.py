import time


def pow(num,power):
    return num ** power
def time_taken(num,power): 
    start = time.time()
    val = pow(num,power)
    end = time.time()  
    
    print("{0} raise to the power {1} = {2}".format(num,power,val))
    print()
    print("time diffrence is {0}".format(end - start))

num = int(input("enter number "))
power = int(input("Enter Power ::"))

time_taken(num,power)


            