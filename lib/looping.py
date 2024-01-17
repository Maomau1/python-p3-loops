#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    i=10
    while i > 0 :
        print(f"{i}")
        i -=1
    print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    pass
    return [integer*integer for integer in int_list]

def fizzbuzz():
    # code goes here!
    pass
    for i in range(100) :
        if (i+1) % 3 == 0 and (i+1) % 5 == 0 :
            print ("FizzBuzz")
        elif (i+1) % 5 == 0 :
            print("Buzz")
        elif (i+1) % 3 == 0 :
            print("Fizz")
        else :
            print(f"{i+1}")
