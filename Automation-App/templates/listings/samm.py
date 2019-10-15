class swapping:
    def swap(self,a,b):
        a=a+b
        b=a-b
        a=a-b
        return (a,b)

l = swapping()
m = l.swap(2,3)
print(m)