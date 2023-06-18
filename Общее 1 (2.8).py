def test():
    number = int(input("Enter an enteger : "))
    if number > 0:
     positive()
    else:
        negative()

def positive():
    print("Positive")
def negative():
    print("Negative")
test()