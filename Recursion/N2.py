def fib(n):
    ls = [1, 1]

    def fib(lst, no):
        if len(lst) < no:
            lst.append(lst[-1] + lst[-2])
            return fib(lst,no)
        else:
            return lst

    return(fib(ls, no=n)[-1])
