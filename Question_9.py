def string(k):
    l=[]
    for i in k:
        for j in range(0,255):
            if i==chr(j):
                l.append([i,j])



    return l
s="python"
print(string(s))