def fruit(basket="apple"):
    print("fruit")
    def apple():
        return "apple"
    def orange():
        return "orange"
    if basket=="apple":
        return apple
    else:
        return orange

vega=fruit()
print(vega())