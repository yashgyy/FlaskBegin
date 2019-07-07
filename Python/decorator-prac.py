def controller(func):
    def explicit():
        print("Calculating 2+2")
        func()
        print("End of Calculating 2+2")
    return explicit

def func():
    print(2+2)

func()

@controller  #Passed Here and Returned Here
def func1():
    print(2+2)

func1()