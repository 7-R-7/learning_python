from time import time

def speedTest(func):
    def wrapper():

        start = time()

        func()

        end = time()

        print(f"Function Running Time Is : {end - start}")

    return wrapper

@speedTest
def Loop_Func():

    for number in range(1, 12345):
        print(number)
    
Loop_Func()
