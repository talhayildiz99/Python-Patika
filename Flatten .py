# [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(x=[[1,'a',['cat'],2],[[[3]],'dog'],4,5],yeni=[]):
     for e in x:
        if type(e)== list:
            flatten(e,yeni)
        else:
            yeni.append(e)
     return yeni
print(flatten())



