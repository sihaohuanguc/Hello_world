def test_args(*argv):
    print_str=[]
    for arg in argv:
        print_str.append(arg)
    print("".join(print_str))

test_args("Hel","l","o wo","rld!")
