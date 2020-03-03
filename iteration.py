def generate_index(n):
    for i in range(n):
        yield i+1 

my_string="Hello World!"
my_iter=iter(my_string)
for index in generate_index(len(my_string)):
    print(str(index)+"-"+next(my_iter))