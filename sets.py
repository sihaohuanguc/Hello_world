list_a=["or","lo w","or","","lo w","lo w"]
list_b=["k","v","pi","Hel","P","L"," ","Hel","l","lo","a","el","p","dl","lo w","w"]
list_c=["o","H","ld","lo w","ld","L","or","l"," w","pl","ld","d","d"]
set_a=set(list_a)
set_b=set(list_b)
good=set([item for item in list_b if list_b.count(item)>1]) #Hel
better=set_b.intersection(set_a) #lo w
best=set_b.union(set_a)
glad=set_a.difference(set_b) #or
interesting=set([item for item in list_c if list_c.count(item)>2]) #ld
print("".join(list(good)+list(better)+list(glad)+list(interesting)+list("!")))