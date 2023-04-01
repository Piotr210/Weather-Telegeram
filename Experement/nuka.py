def maus(func):
    def ima(a,b):
        d=func(a,b)
        return d
    return ima(3,4)

def pink(slag1,slag2):
    k=slag1+slag2
    return k

print(maus(pink))