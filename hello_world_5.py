class DNA_computer(object):
    def __init__(self):
        pass
    def replace_code(self,read):
        read=read.replace("A","0")
        read=read.replace("C","1")
        read=read.replace("G","2")
        read=read.replace("T","3")
        return read
    def decoder(self,read):
        if not len(read)%4==0:
            print("Code length error!")
        else:
            this_is_what=[]
            read=self.replace_code(read)
            for i in range(int(len(read)/4)):
                ascii_value=int(read[4*i])*64+int(read[4*i+1])*16+int(read[4*i+2])*4+int(read[4*i+3])
                this_is_what.append(chr(ascii_value))
            interval=""
            print(interval.join(this_is_what))


read="CAGACGCCCGTACGTACGTTAGAACTCTCGTTCTAGCGTACGCAAGAC"
comp=DNA_computer()
comp.decoder(read)
# However, mutations easily destroy the information.
