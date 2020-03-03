def reciprocal(x):
    return 1/x
def opposite(x):
    return -x
def odd(x):
    return x**4-4*x**3+27

func=[reciprocal,opposite,odd]
for i in range(1,10):
    values=map(lambda x:x(i),func)
    print(list(values))