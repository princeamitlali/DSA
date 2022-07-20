import time


def count_set(num):
    res = 0
    while num > 0 :
        if num % 2 != 0:
            res += 1
        num = num //2
    return res
    
def time_taken(num): 
    start = time.time()
    val = count_set(num)
    end = time.time()  
    
    print("{0} number of bit  is set in {1}".format(val,num))
    print()
    print("time diffrence is {0}".format(end - start))

num = int(input("enter number "))


time_taken(num)


            