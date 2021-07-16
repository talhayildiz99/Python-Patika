l = [[1, 2], [3, 4], [5, 6, 7]]
def reversing(x):
    a=[]
    b=[]
    for i in x:
        a.append(i[::-1])
    b=a[::-1]
    return b
print(reversing(l))
