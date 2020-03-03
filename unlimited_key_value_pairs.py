def test_args(fixed,*args,**kwargs):
    a=[fixed]
    for arg in args:
        a.append(arg)
    for key,value in kwargs.items():
        a.append(key)
        a.append(value)
    print("".join(a))

happy=("el","l")
glad={"o":" ","wo":"r","l":"d!"}
test_args("H",*happy,**glad)
