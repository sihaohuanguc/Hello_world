words=["Hel","apple","lo ","w","Fantastic!","orl","Math is useful.","object","d!","just business","Happy"]
shorter=filter(lambda x:len(x)<5,words)
print("".join(shorter))