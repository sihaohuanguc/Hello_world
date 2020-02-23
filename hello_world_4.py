what_is_this=[]
this_is_what=[]
what_is_this.append(72)
what_is_this.append(101)
for i in range(2):
    what_is_this.append(108)
for i in range(2):
    what_is_this.append(111)
what_is_this.insert(5,119)
what_is_this.insert(5,32)
what_is_this.extend([114,108,100,33])

for i in range(len(what_is_this)):
    this_is_what.append(chr(what_is_this[i]))

interval=""
print(interval.join(this_is_what))