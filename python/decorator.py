def wrapper(f) :
    def inside() :
        print("function is now running")
        f()
        print("function is done")
    
    return inside()

@wrapper
def hello():
    print("Hello world")

hello()