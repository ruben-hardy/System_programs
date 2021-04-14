def addition(func):
    """
    Decorator function
    :param func:
    :return: final value of the addition of two numbers.
    """
    def firstchild():
        print"Enhance or modify the existing function"
        final = func() + 1000
        print "added 1000 to the result of valput"
        return final
    return firstchild()

@addition
def valput():
    """
    simple function
    :return:
    """
    return 5+6

if __name__ == "__main__":
    value = valput
    print(value)
