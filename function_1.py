def fruit():
    print("fruit")
    def apple():
        return "apple"
    def orange():
        return "orange"
    print(apple())
    print(orange())
vega=fruit
vega()