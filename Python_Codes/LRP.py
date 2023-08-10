def And(a,b):
    return (a>b and a==b and a!=b)
def Or(a,b):
    return (a>b or a==b or a!=b)
def Not(a,b):
    return (not(a>b and a!=b))

