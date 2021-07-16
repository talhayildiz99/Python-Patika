# [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(x=[[1,'a',['cat'],2],[[[3]],'dog'],4,5],new=[]):
     for e in x:
        if type(e)== list:
            flatten(e,new)
        else:
            new.append(e)
     return new
print(flatten())



